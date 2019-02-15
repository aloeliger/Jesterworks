#Andrew Loeliger
#Skim code. 
#Requires outside input of a configuration file, and a small dedicated
#.py file that defines what a good event is off of the chain, and takes a sample name
# then it defines a function that defines which events to prioritize in case
# of duplicates
# then it creats an instance, gives it these functions, and runs it.
import ROOT
import os, sys, configparser
import glob
from tqdm import tqdm
from array import array
import ctypes
import threading
import Queue

#default version of a skim function. Tells you what to actually do
def DefaultSkimFunction(TheEvent):
    print("Proper Skim function not defined! Defaulting to rejecting all events!")
    print("Please define a skim function that takes two argument: The Chain (with current values grabbed) and a sample name.")
    print("As well as a main function that creates a Jesterworks instance, and gives it a proper configuration and this function.")
    return False

#default version of a priority function. Tells you what to actually do
def DefaultPriorityFunction(NewEventDictionary,OldEventDictrionary):
    print("Proper Priority Function not defined! Defaulting to keeping the first event!")
    print("Please define a function that takes two dictionaries.")
    print("The first will be the new event, with keys named after the branches")
    print("The second will be the old event, defined similarly")
    print("It should return true if we keep the new event")
    print("false otherwise")
    return False

#Takes the chain and really quickly creates the combined RLE code to check 
#things against.
def GetRLECode(TheEvent):
    return str(TheEvent.run)+":"+str(TheEvent.lumi)+":"+str(TheEvent.evt)

queueLock = threading.Lock()
threadLock = threading.Lock()
WorkQueue = Queue.Queue()
IDQueue = Queue.Queue()

#the thread takes the Jesterworks instance it was called from as an argument
#a large amount of the variables that don't change to file to file should be
#mirrored exactly here so that the skim process doesn't have to change massively
class SkimThread(threading.Thread):
    def __init__(self,JesterworksInstance):
        self.TheJesterworksInstance = JesterworksInstance
    def run(self):
        self.TheJesterworksInstance.ThreadHandle()

class Jesterworks():
    #takes a configuration, a skimming function, and a priority function
    #The skim function will be used later to decide if an event passes,
    #the priority function will be used to decide between duplicate pairs of events.
    def __init__(self,ConfigFileName = "",
                 SkimFunctionDefinition=DefaultSkimFunction,
                 PriorityFunctionDefinition=DefaultPriorityFunction):
        self.Configuration = configparser.ConfigParser()
        self.Configuration.optionxform = str
        self.Configuration.read(ConfigFileName)
        self.OutTreeName = ""
        self.OutFileName = ""
        self.InputChainName = ""
        self.Channel = ""
        self.NumFilesToProcess = ""
        self.SampleName = ""
        self.GrabHistos = True
        self.RenameDictionary = {}
        self.InputFiles = []
        self.PathList = []    
        self.PerformPreCuts = False
        self.PreCutList = []
        self.AltGrabHistos = False
        self.CancelationList = []
        self.SkimEvalFunction = SkimFunctionDefinition
        self.PriorityEvalFunction = PriorityFunctionDefinition
        self.Threads=[]

        print("Processing Configuration...")
        for Token in self.Configuration:
            for Element in self.Configuration[Token]:                
                if(Token == "OUTPUT"):
                    if(Element == "tree"):
                        self.OutTreeName = str(self.Configuration[Token][Element])
                        print("OutTreeName: "+self.OutTreeName)
                    if(Element == "file"):
                        self.OutFileName = str(self.Configuration[Token][Element])
                        print("OutFileName: "+self.OutFileName)
                    if(Element == "grabhistos"):
                        if self.Configuration[Token][Element] == "False":
                            self.GrabHistos = False
                        elif self.Configuration[Token][Element] == "True":
                            self.GrabHistos = True
                        print("GrabHistos: "+str(self.GrabHistos))
                    if(Element == "altgrabhistos"):
                        if self.Configuration[Token][Element] == "False":
                            self.AltGrabHistos = False
                        elif self.Configuration[Token][Element] == "True":
                            self.AltGrabHistos = True
                        print("AltGrabHistos: "+str(self.GrabHistos))

                if(Token == "INPUT"):
                    if(Element == "chain"):
                        self.InputChainName = str(self.Configuration[Token][Element])
                        print("InputChainName: "+self.InputChainName)
                    if(Element == "path"):
                        self.PathList = self.Configuration[Token][Element].splitlines()
                        print("PathList: ")
                        print(self.PathList)
                    if(Element == "numfiles"):                        
                        self.NumFilesToProcess = str(self.Configuration[Token][Element])
                        print("NumFilesToProcess: "+self.NumFilesToProcess)
                    if(Element == "channel"):
                        self.Channel = str(self.Configuration[Token][Element])
                        print("Channel: "+self.Channel)
                    if(Element == "sample"):
                        self.SampleName = str(self.Configuration[Token][Element])
                        print("SampleName: "+self.SampleName)
                        
                if(Token == "RENAME"):
                    self.RenameDictionary[Element] = str(self.Configuration[Token][Element])
                if(Token == "CANCEL"):
                    self.CancelationList.append(str(self.Configuration[Token][Element]))
                if(Token == "PRECUTS"):
                    self.PerformPreCuts = True
                    self.PreCutList.append(str(self.Configuration[Token][Element]))
        print("Done Processing Configuration")            
        
    #Just generates a list of file paths that we can use later to hook trees
    #up to the relevant chain.
    def CreateListOfFilesToRunOn(self):
        print("Generating List of Files To Run On...")
        if (self.NumFilesToProcess == "all" or self.NumFilesToProcess == "0"):
            for Path in self.PathList:
                for Filename in glob.glob(Path+"*"):                    
                    self.InputFiles.append(Filename)
        else:            
            NumFilesGrabbed = 0
            for Path in self.PathList:                                
                if (NumFilesGrabbed == int(self.NumFilesToProcess)):
                    break                
                for Filename in glob.glob(Path+"*"):
                    self.InputFiles.append(Filename)
                    NumFilesGrabbed += 1
                    if (NumFilesGrabbed == int(self.NumFilesToProcess)):
                        break
        print("Done Generating List of Files To Run On...")

    def RunOnListOfFiles(self):
        for i in range(len(self.InputFiles)):
            print("File: "+str(self.InputFiles[i]))
            self.PerformSkim(self.InputFiles[i],i)

    def GenerateThreads(self):
        print("Generating the list of threads...")
        print(self.InputFiles)
        #first things first, let's get names and thread numbers
        #put those in a queue, and then we'll make like 6 threads
        #and while there's something to do, each thread can pop
        # a file and a number off of a queue, then get about runninng it.
        queueLock.acquire()
        for i in range(len(self.InputFiles)):
            WorkQueue.put(self.InputFiles[i])
            IDQueue.put(i)
        queueLock.acquire()

        threadLock.acquire()
        for i in range(6):
            TheThread = SkimThread(self)
            TheThread.start()
            self.Threads.append(TheThread)
        threadLock.release()

        for i in range(len(self.Threads)):
            self.Threads[i].join()


    #Here's where we do the all important skimming job.    
    #it's designed to be handed to a thread, so the self calls here 
    def PerformSkim(self,TheFile,Index):
        print("Performing Skim...")
        print("\tSetting Up Output File...")
        OutputFile = ROOT.TFile(self.OutFileName+"_"+str(Index)+".root","RECREATE")                

        print("\tSetting Up Input Chain...")
        AdditionalSlash = "/"
        if self.Channel == "":
            #no need to prepend a slash
            AdditionalSlash = ""
        InputChain = ROOT.TChain(self.Channel+AdditionalSlash+self.InputChainName)       
        InputChain.Add(TheFile)

        #creates output tree, and a dictionary it reads from
        print("\tSetting Up Output Tree...")
        OutputTreeDictionary = {}
        OutputTree = ROOT.TTree(self.OutTreeName,self.OutTreeName)
        for Branch in InputChain.GetListOfBranches():
            ExpectedClass = ROOT.TClass()
            ExpectedType = ctypes.c_long(0)
            Branch.GetExpectedType(ExpectedClass,ExpectedType)
            if(ExpectedType.value == ROOT.kInt_t):
                Value = array('I',[0])
                OutputTree.Branch(Branch.GetName(),Value,Branch.GetName()+"/i")
                OutputTreeDictionary[Branch.GetName()] = Value
            elif (ExpectedType.value == ROOT.kLong_t):
                Value = array('l',[0])                
                OutputTree.Branch(Branch.GetName(),Value,Branch.GetName()+"/l")
                OutputTreeDictionary[Branch.GetName()] = Value                
            else:
                Value = array('f',[0.])                
                OutputTree.Branch(Branch.GetName(),Value,Branch.GetName()+"/F")
                OutputTreeDictionary[Branch.GetName()] = Value                
        #cancelations:
        print("\tPerforming cancelations...")
        for Item in self.CancelationList:
            OutputTree.GetBranch(Item).SetStatus(0)

        #precutting, hopefully speeds up skims
        #the cut string provided shouldn't need to access the full tree
        #entry the same way that a GetEntry call might.
        if(self.PerformPreCuts):
            print("\tPerforming precutting...")
            CompleteCut = ""
            for Cut in self.PreCutList:
                CompleteCut+=("("+Cut+")&&")
            CompleteCut=CompleteCut[:len(CompleteCut)-2]
            InputChain = InputChain.CopyTree(CompleteCut)        
        
        #provide dictionaries in the same vein as the output tree dictoinary
        #one will be to hold the current prefered version of an event "old"
        #the other to hold whichever one we are reading now "new"
        print("\tSetting up the event dictionaries...")
        EventValues = {}
        NewEventDictionary={}
        OldEventDictionary={}
        for Branch in InputChain.GetListOfBranches():
            ExpectedClass = ROOT.TClass()
            ExpectedType = ctypes.c_long(0)
            Branch.GetExpectedType(ExpectedClass,ExpectedType)
            if(ExpectedType.value == ROOT.kInt_t):
                EventValues[Branch.GetName()] = array('I',[0])
                Branch.SetAddress(EventValues[Branch.GetName()])
            elif(ExpectedType.value == ROOT.kLong_t):
                EventValues[Branch.GetName()] = array('l',[0])
                Branch.SetAddress(EventValues[Branch.GetName()])
            else:
                EventValues[Branch.GetName()] = array('f',[0.])
                Branch.SetAddress(EventValues[Branch.GetName()])        

        print("\tRunning The Chain...")        
        #Here's where the skim really happens, selection handled 
        #via passed function.    
        PreferedRLE = ''
        FirstAcceptedEvent = True
        for i in tqdm(range(InputChain.GetEntries())):            
            InputChain.GetEntry(i)            
            if self.SkimEvalFunction(InputChain,self.SampleName):
                #Good event. Automatically fill The new event dictionary.
                for key in EventValues:
                    NewEventDictionary[key] = EventValues[key][0]
                #if it's the first event, automatically dump this to the prefered event dictionary and continue
                if(FirstAcceptedEvent):                    
                    OldEventDictionary = NewEventDictionary
                    FirstAcceptedEvent = False
                    continue
                #otherwise if it's not and we have a duplicate, find the prefered, dump it to prefered
                elif(GetRLECode(InputChain) == PreferedRLE and not FirstAcceptedEvent):
                    if(self.PriorityEvalFunction(NewEventDictionary,OldEventDictionary)):                        
                        PreferedRLE = GetRLECode(InputChain)
                        OldEventDictionary = NewEventDictionary
                    else:                        
                        continue
                #otherwise, we have a non duplicate, put the old tree values in the Output dictionary, and fill
                elif(GetRLECode(InputChain) != PreferedRLE and not FirstAcceptedEvent):                    
                    for key in OldEventDictionary:                        
                        OutputTreeDictionary[key][0] = OldEventDictionary[key]                        
                    OutputTree.Fill()                       
                    PreferedRLE = GetRLECode(InputChain)
                    OldEventDictionary = NewEventDictionary
            else:                
                continue

        #the loop leaves us with a good event queued, fill it.
        for key in OldEventDictionary:
            OutputTreeDictionary[key][0] = OldEventDictionary[key]
        OutputTree.Fill()                                        

        #grab the important histogram that come along with
        if(self.GrabHistos):
            #print("\tCreating Meta Histograms...")
            InitialFile = ROOT.TFile(self.InputFiles[0],"READ")
            EventCounter = InitialFile.Get(self.Channel+AdditionalSlash+"eventCount").Clone()
            EventCounter.SetDirectory(0)
            EventCounterWeights = InitialFile.Get(self.Channel+AdditionalSlash+"summedWeights").Clone()
            EventCounterWeights.SetDirectory(0)            
            InitialFile.Close()        
            for i in range(1,len(self.InputFiles)):
                TheFile = ROOT.TFile(self.InputFiles[i],"READ")
                EventCounter.Add(TheFile.Get(self.Channel+AdditionalSlash+"eventCount"))
                EventCounterWeights.Add(TheFile.Get(self.Channel+AdditionalSlash+"summedWeights"))
                TheFile.Close()                            
        if(self.AltGrabHistos):
            #print("\tGrabbing alternate meta histograms (Cecile names)...")
            InitialFile = ROOT.TFile(self.InputFiles[0],"READ")
            EventCounter = InitialFile.Get("nevents").Clone()
            EventCounter.SetDirectory(0)
            InitialFile.Close()
            for i in range(1,len(self.InputFiles)):
                TheFile = ROOT.TFile(self.InputFiles[i],"READ")
                EventCounter.Add(TheFile.Get("nevents"))
                TheFile.Close()
            EventCounter.SetNameTitle("eventCount","eventCount")
            
        #Post skim
        #print("\tPerforming Renaming...")
        for key in self.RenameDictionary:
            print("\t\t"+key+" -> "+self.RenameDictionary[key])
            OutputTree.GetBranch(key).SetNameTitle(self.RenameDictionary[key],self.RenameDictionary[key])

        #print("\tWriting To File... ")
        #OutputTree.SetDirectory(0)
        OutputFile.cd()
        OutputTree.Write()
        if(self.GrabHistos or self.AltGrabHistos):
            EventCounter.Write()
        if(self.GrabHistos):            
            EventCounterWeights.Write()
        OutputFile.Write()
        OutputFile.Close()
        print("Done Performing Skim...")

    def ThreadHandle(self):
        #do we have something to do?
        SomethingToDo = True
        IndexNum = 0
        FilePath = ""
        while SomethingToDo:
            queueLock.acquire()
            if WorkQueue.empty():
                somethingToDo = False
                queueLock.acquire()
            else:
                IndexNum = IDQueue.get()
                FilePath = WorkQueue.get()
                queueLock.release()
                self.PerformSkim(FilePath,IndexNum)
if __name__ == "__main__":
    print("Can't call this file. Please create a specific file with a skimming function(takes a chain with values ready to go as an argument and a sample name, returns true if this event is to be accepted, and false otherwise), a priority function (takes two dictionaries with branch name keys, returns true to keep the new event, false otherwise) and a main that creates a tau skim instance, and gives it both a configuration file, and these functions.")
