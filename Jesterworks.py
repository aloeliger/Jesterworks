#!/usr/bin/env python
#Author: Andrew Loeliger
import ROOT
import os, sys, configparser
from tqdm import tqdm
from array import array
class Jesterworks():
    def __init__(self,ConfigFileName = ""):
        self.Configuration = configparser.ConfigParser()
        self.Configuration.read(ConfigFileName)                        
        self.RenameDictionary = {}
        self.Path = ""
        self.OutTreeName = ""
        self.InputFiles = []        
        self.CutList = []        
        self.FirstLoadedFile = True        
        self.pileup_mc = ROOT.TH1F("pileup_mc","pileup_mc", 80, 0.0, 80.0)
    
    def ProcessConfiguration(self):        
        for Token in self.Configuration:
            for Element in self.Configuration[Token]:                
                #print("Token: "+Token)
                #print("Element: "+Element)
                #print("Value: "+self.Configuration[Token][Element])
                #print()
                if(Token == "RENAME"):                   
                    self.RenameDictionary[Element] = self.Configuration[Token][Element]

                if(Token == "CUTS"):
                    self.CutList.append(self.Configuration[Token][Element])
                
                if(Token == "OUTPUT"):
                    if(Element == "tree"):
                        self.OutTreeName = self.Configuration[Token][Element]
                    if(Element == "file"):
                        self.OutFile = ROOT.TFile(self.Configuration[Token][Element],"RECREATE");
                
                if(Token == "INPUT"):
                    if(Element == "chain"):
                        #print("Making a chain! Yay!")
                        self.InputChain = ROOT.TChain(self.Configuration[Token][Element],self.Configuration[Token][Element])
                    if(Element == "path"):
                        self.Path = self.Configuration[Token][Element]
                    if(Element == "numfiles"):
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
        print("Done Processing Configuration...")        

    def PerformSkim(self):        
        print("Processing Skim...")
        TempTree = self.InputChain.CopyTree("")        
        for i in tqdm(range(len(self.CutList))):
            TempTree = TempTree.CopyTree(self.CutList[i])
        self.OutTree = TempTree        
        self.OutTree.SetNameTitle(self.OutTreeName,self.OutTreeName)
        for Branch in self.OutTree.GetListOfBranches():
            #print(Branch)
            if(Branch.GetName() in self.RenameDictionary.keys()):
                if (self.RenameDictionary[Branch.GetName()] == "cancel"):
                    Branch.SetStatus(0)
                else:
                    Branch.SetNameTitle(self.RenameDictionary[Branch.GetName()])                    
        #should be done now?

    def WrapUpAndLeave(self):
        self.OutFile.cd()
        self.OutTree.Write()
        self.EventCounter.Write()
        self.EventCounterWeights.Write()
        self.pileup_mc.Write()
        self.OutFile.Close()
            
if __name__ == "__main__":
    JesterworksImplementation = Jesterworks(sys.argv[1])
    JesterworksImplementation.ProcessConfiguration()    
    JesterworksImplementation.PerformSkim()
    JesterworksImplementation.WrapUpAndLeave()
