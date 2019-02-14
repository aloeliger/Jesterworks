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
        print("Running the list of files...")
        if(not self.InputFiles):
            print("\tList of files empty!")
        for i in range(len(self.InputFiles)):
            print("File: "+str(self.InputFiles[i]))
            self.PerformSkim(self.InputFiles[i],i)

    #Here's where we do the all important skimming job.    
    def PerformSkim(self,TheFile,Index):
        print("Performing Skim...")
        print("\tSetting Up Output File...")
        OutputFile = ROOT.TFile(self.OutFileName+"_"+str(Index)+".root","RECREATE")
        
        #print("\tSetting up scratch/working file...")
        #ScratchFile = ROOT.TFile(self.OutFileName+"_Scratch.root","RECREATE")

        print("\tSetting Up Input Chain...")
        AdditionalSlash = "/"
        if self.Channel == "":
            #no need to prepend a slash
            AdditionalSlash = ""
        InputChain = ROOT.TChain(self.Channel+AdditionalSlash+self.InputChainName)
        #for FileName in self.InputFiles:            
        #InputChain.Add(FileName)            
        InputChain.Add(TheFile)

        #Okay, this may be causing errors.
        #let's try creating this with it's own dictionary we read out too.
        #need to fix this so we don't have to hard code the int branches
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

        print("\tPerforming cancelations...")
        for Item in self.CancelationList:
            OutputTree.GetBranch(Item).SetStatus(0)

        if(self.PerformPreCuts):
            print("\tPerforming precutting...")
            CompleteCut = ""
            for Cut in self.PreCutList:
                CompleteCut+=("("+Cut+")&&")
            CompleteCut=CompleteCut[:len(CompleteCut)-2]
            InputChain = InputChain.CopyTree(CompleteCut)        
        
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
            #print("\t\tGetting intial event...")
            InputChain.GetEntry(i)            
            if self.SkimEvalFunction(InputChain,self.SampleName):                
                #print("\t\t\tFound good event...")
                #Good event. Automatically fill The new event dictionary.
                for key in EventValues:
                    NewEventDictionary[key] = EventValues[key][0]
                #if it's the first event, automatically dump this to the prefered event dictionary and continue
                if(FirstAcceptedEvent):
                    #print("\t\t\t\tFirst accepted event, making it prefered and moving on...")
                    OldEventDictionary = NewEventDictionary                    
                    FirstAcceptedEvent = False
                    continue
                #otherwise if it's not and we have a duplicate, find the prefered, dump it to prefered
                elif(GetRLECode(InputChain) == PreferedRLE and not FirstAcceptedEvent):
                    #print("\t\t\t\tDuplicate event...")             
                    if(self.PriorityEvalFunction(NewEventDictionary,OldEventDictionary)):
                        #print("\t\t\t\t\tKeeping new event...")
                        PreferedRLE = GetRLECode(InputChain)
                        OldEventDictionary = NewEventDictionary
                    else:
                        #print("\t\t\t\t\tKeeping old event...")
                        continue
                #otherwise, we have a non duplicate, put the old tree values in the Output dictionary, and fill
                elif(GetRLECode(InputChain) != PreferedRLE and not FirstAcceptedEvent):
                    #print("\t\t\t\tNon duplicate event, filling...")                                        
                    for key in OldEventDictionary:                        
                        OutputTreeDictionary[key][0] = OldEventDictionary[key]                        
                    OutputTree.Fill()                       
                    PreferedRLE = GetRLECode(InputChain)
                    OldEventDictionary = NewEventDictionary
            else:
                #print("\t\t\tFound bad event...")
                continue
        #the loop leaves us with a good event queued, fill it.
        for key in OldEventDictionary:
            OutputTreeDictionary[key][0] = OldEventDictionary[key]
        OutputTree.Fill()                                        

        #grab the important histogram that come along with
        if(self.GrabHistos):
            print("\tCreating Meta Histograms...")
            InitialFile = ROOT.TFile(TheFile,"READ")
            EventCounter = InitialFile.Get(self.Channel+AdditionalSlash+"eventCount").Clone()
            EventCounter.SetDirectory(0)
            EventCounterWeights = InitialFile.Get(self.Channel+AdditionalSlash+"summedWeights").Clone()
            EventCounterWeights.SetDirectory(0)            
            InitialFile.Close()        
            #for i in range(1,len(self.InputFiles)):
            #    TheFile = ROOT.TFile(self.InputFiles[i],"READ")
            #    EventCounter.Add(TheFile.Get(self.Channel+AdditionalSlash+"eventCount"))
            #    EventCounterWeights.Add(TheFile.Get(self.Channel+AdditionalSlash+"summedWeights"))
            #    TheFile.Close()                            
        if(self.AltGrabHistos):
            print("\tGrabbing alternate meta histograms (Cecile names)...")
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
        print("\tPerforming Renaming...")
        for key in self.RenameDictionary:
            #print("\t\t"+key+" -> "+self.RenameDictionary[key])
            try:
                OutputTree.GetBranch(key).SetNameTitle(self.RenameDictionary[key],self.RenameDictionary[key])
            except:
                print("\t\tFailed to rename: "+key+" -> "+self.RenameDictionary[key])

        print("\tWriting To File... ")
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

if __name__ == "__main__":
    print("Can't call this file. Please create a specific file with a skimming function(takes a chain with values ready to go as an argument and a sample name, returns true if this event is to be accepted, and false otherwise), a priority function (takes two dictionaries with branch name keys, returns true to keep the new event, false otherwise) and a main that creates a tau skim instance, and gives it both a configuration file, and these functions.")
