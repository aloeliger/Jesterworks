#!/usr/bin/env python
#Author: Andrew Loeliger
import ROOT
import os, sys, configparser
import threading
from tqdm import tqdm
from array import array

ThreadLock = threading.Lock()

class SkimThread(threading.Thread):
    def __init__(self,RunFunction,ProcessNumber,OutTreeName,OutFileName,
                 InputChainName,FileToSkimName,TheCuts,RenameDictionary):
        threading.Thread.__init__(self)        
        self.ProcessNumber = ProcessNumber
        self.OutTreeName = OutTreeName
        self.OutFileName = OutFileName
        self.InputChainName = InputChainName
        self.FileToSkimName = FileToSkimName
        self.TheCuts = TheCuts
        self.RenameDictionary = RenameDictionary
        self.RunFunction = RunFunction         
    def run(self):
        self.RunFunction(self.ProcessNumber,self.OutTreeName,
                         self.OutFileName,self.InputChainName,
                         self.FileToSkimName,self.TheCuts,
                         self.RenameDictionary)

class Jesterworks():
    def __init__(self,ConfigFileName = ""):
        self.Configuration = configparser.ConfigParser()
        self.Configuration.read(ConfigFileName)                        
        self.RenameDictionary = {}        
        self.OutTreeName = ""
        self.OutFileName = ""
        self.InputChainName = ""
        self.PathList = []
        self.NumFilesToProcess = ""
        self.InputFiles = []        
        self.CutList = []        
        self.FirstLoadedFile = True   
        self.Threads = []
        self.ProcessConfiguration()
        self.CreateListOfFilesToRunOn()
    
    def ProcessConfiguration(self):        
        print("Processing Configuration...")
        for Token in self.Configuration:
            for Element in self.Configuration[Token]:                                
                if(Token == "RENAME"):                   
                    self.RenameDictionary[Element] = self.Configuration[Token][Element]

                if(Token == "CUTS"):
                    self.CutList.append(self.Configuration[Token][Element])
                
                if(Token == "OUTPUT"):
                    if(Element == "tree"):
                        self.OutTreeName = self.Configuration[Token][Element]
                    if(Element == "file"):
                        self.OutFileName = self.Configuration[Token][Element]
                
                if(Token == "INPUT"):
                    if(Element == "chain"):                        
                        self.InputChainName = self.Configuration[Token][Element]
                    if(Element == "path"):
                        self.PathList = self.Configuration[Token][Element].splitlines()
                    if(Element == "numfiles"):
                        self.NumFilesToProcess = self.Configuration[Token][Element]
        print("Done Processing Configuration...")        

    def CreateListOfFilesToRunOn(self):
        print("Generating List of Files To Run On...")
        if (self.NumFilesToProcess == "all" or self.NumFilesToProcess == "0"):
            for Path in self.PathList:
                for Filename in os.listdir(Path):
                    self.InputFiles.append(Path+Filename)
        else:
            NumFilesGrabbed = 0
            for Path in self.PathList:
                if (NumFilesGrabbed == int(self.NumFilesToProcess)):
                    break
                for Filename in os.listdir(Path):
                    self.InputFiles.append(Path+Filename)
                    NumFilesGrabbed += 1
                    if (NumFilesGrabbed == int(self.NumFilesToProcess)):
                        break

    def PerformSkim(self,ProcessNumber,OutTreeName,OutFileName,InputChainName,FileToSkimName,TheCuts,RenameDictionary):
        #Create the file, 
        OutFile = ROOT.TFile(OutFileName+"_"+str(ProcessNumber)+".root", "RECREATE")
        
        #just create a scratch file for root to have disc access
        ScratchFile = ROOT.TFile("Scratch_"+str(ProcessNumber)+".root","Recreate")
        ScratchFile.cd()

        #setup the input        
        InputChain = ROOT.TChain(InputChainName)
        InputChain.Add(FileToSkimName)
        InputChain.SetDirectory(0)        

        #perform the skim now.        
        TempTree = InputChain.CopyTree("")        
        for Cut in TheCuts:
            TempTree = TempTree.CopyTree(Cut)
        OutTree = TempTree
        OutTree.SetNameTitle(OutTreeName,OutTreeName)

        #perform any renaming        
        for Branch in OutTree.GetListOfBranches():            
            if(Branch.GetName() in RenameDictionary.keys()):
                if (RenameDictionary[Branch.GetName()] == "cancel"):
                    Branch.SetStatus(0)
                else:
                    Branch.SetNameTitle(RenameDictionary[Branch.GetName()])                    

        #make the first two histograms
        TheFileToSkim = ROOT.TFile(FileToSkimName,"READ")
                
        EventCounter = TheFileToSkim.Get("mt/eventCount").Clone()
        EventCounterWeights = TheFileToSkim.Get("mt/summedWeights").Clone()
        EventCounter.SetDirectory(0) #Don't lose the histograms when file closes
        EventCounterWeights.SetDirectory(0)

        #make PileupMC Histogram
        pileup_mc  = ROOT.TH1F("pileup_mc","pileup_mc",80,0,80)
        for Event in InputChain:
            pileup_mc.Fill(InputChain.nTruePU)
        
        #write things, and leave
        #ThreadLock.acquire()
        OutFile.cd()
        OutTree.Write()
        EventCounter.Write()
        EventCounterWeights.Write()
        pileup_mc.Write()
        OutFile.Write()
        OutFile.Close()
        #ThreadLock.release()        

    def DelegateSkimmingJobs(self):
        print("Delegating Skimming Jobs...")
        Processed = 0        
        for File in self.InputFiles:
            TheThread = SkimThread(self.PerformSkim,Processed,
                                   self.OutTreeName,self.OutFileName,
                                   self.InputChainName,File,
                                   self.CutList,self.RenameDictionary)
            TheThread.start()
            self.Threads.append(TheThread)
            Processed+=1
        for i in tqdm(range(len(self.Threads))):
            self.Threads[i].join()
            
if __name__ == "__main__":
    JesterworksImplementation = Jesterworks(sys.argv[1])    
    JesterworksImplementation.DelegateSkimmingJobs()

#keep this code around to serve as an example of how to go about the histogram creation
""" 
                        if (self.Configuration[Token][Element] == "all" or self.Configuration[Token][Element] == "0"):
                            for Filename in os.listdir(self.Path):
                                self.InputChain.Add(self.Path+"/"+Filename)
                                HistoFile = ROOT.TFile(self.Path+"/"+Filename,"READ")
                                if(FirstLoadedFile):
                                    self.EventCounter = HistoFile.Get("mt/eventCount").Clone()
                                    self.EventCounterWeights = HistoFile.Get("mt/summedWeights").Clone()
                                    self.FirstLoadedFile = False
                                else:
                                    NewHistoFile = ROOT.TFile(self.Path+"/"+Filename,"READ")
                                    self.EventCounter.Add(NewHistoFile.Get("mt/eventCount").Clone())
                                    self.EventCounterWeights.Add(NewHistoFile.Get("mt/summedWeights").Clone())
                                    NewHistoFile.Close()
                        else:
                            for Filename in os.listdir(self.Path)[:int(self.Configuration[Token][Element])]:
                                self.InputChain.Add(self.Path+"/"+Filename)
                                HistoFile = ROOT.TFile(self.Path+"/"+Filename,"READ")                          
                                if(self.FirstLoadedFile):                                    
                                    self.EventCounter = HistoFile.Get("mt/eventCount").Clone()
                                    self.EventCounterWeights = HistoFile.Get("mt/summedWeights").Clone()
                                    self.EventCounter.SetDirectory(0) #Don't lose the histograms when file closes
                                    self.EventCounterWeights.SetDirectory(0)
                                    HistoFile.Close()
                                    self.FirstLoadedFile = False
                                else:                                    
                                    self.EventCounter.Add(HistoFile.Get("mt/eventCount").Clone())
                                    self.EventCounterWeights.Add(HistoFile.Get("mt/summedWeights").Clone())
                                    HistoFile.Close()
"""
