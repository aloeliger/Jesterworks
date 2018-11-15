#!/usr/bin/env python
#Author: Andrew Loeliger
import ROOT
import os, sys, configparser
from tqdm import tqdm
from array import array
from EventManager import EventManager
class Jesterworks():
    def __init__(self,ConfigFileName = ""):
        self.Configuration = configparser.ConfigParser()
        self.Configuration.read(ConfigFileName)        
        self.TheEventManager = EventManager()
        self.CancelationList = []
        self.RenameDictionary = {}
        self.Path = ""
        self.File = ""
        self.CutDictionary = {}
        self.PriorityScheme = ""
        self.FirstLoadedFile = True
        self.pileup_mc = ROOT.TH1F("pileup_mc","pileup_mc", 80, 0.0, 80.0)
    
    def ProcessConfiguration(self,Configuration):
        for Token in self.Configuration:
            for Element in self.Configuration[Token]:                
                if(Token == "rename"):
                    if(self.Configuration[Token][Element] == "cancel"):
                        self.CancelationList.append(Element)
                    else:
                        self.RenameDictionary[Element] = self.Configuration[Token][Element]
                if(Token == "cuts"):
                    self.CutDictionary[Element] = self.Configuration[Token][Element]
                if(Token == "output"):
                    if(Element == "tree"):
                        self.OutTree = ROOT.TTree(self.Configuration[Token][Element],self.Configuration[Token][Element])
                    if(Element == "file"):
                        self.OutFile = ROOT.TFile(self.Configuration[Token][Element],"RECREATE");
                if(Token == "input"):
                    if(Element == "chain"):
                        self.InputChain = ROOT.TChain(self.Configuration[Token][Element],self.Configuration[Token][Element])
                    if(Element == "path"):
                        self.Path = self.Configuration[Token][Element]
                    if(Element == "file"):
                        self.InputChain.Add(self.Path+"/"+self.Configuration[Token][Element])
                        HistoFile = ROOT.TFile(self.Path+"/"+self.Configuration[Token][Element],"READ")
                        if(FirstLoadedFile):
                            self.EventCounter = HistoFile.Get("mt/eventCount").Clone()
                            self.EventCounterWeights = HistoFile.Get("mt/summedWeights").Clone()
                            FirstLoadedFile = False
                        else:
                            self.EventCounter.Add(HistoFile.Get("mt/eventCount").Clone())
                            self.EventCounterWeights.Add(HistoFile.Get("mt/summedWeights").Clone())
                if(Token == "priority"):
                    self.PriortyScheme = self.Configuration[Token][Element]
        print("Done Processing Configuration...")

        def PrepEventManager(self):
            self.TheEventManager.GetInputBranchNameList() = self.InputChain.GetListOfBranches()
            #let's handle the cancelations right here
            for Name in self.CancelationList:
                self.TheEventManager.GetInputBranchNameList().remove(Name)
            #construct the output branches and the translation between input and output in one go
            for Name in self.TheEventManager.GetInputBranchNameList():
                if(self.RenameDictionary[Name] != None):
                    self.TheEventManager.GetInputBranchNameList().append(RenameDictionary[Name])
                    self.TheEventManager.GetTranslationDictionary()[Name] = RenameDictionary[Name]
                else:
                    self.TheEventManager.GetInputBranchNameList().append(Name)
                    self.TheEventManager.GetTranslationDictionary()[Name] = [Name]
            self.TheEventManager.AttachInputChainToVariables(self.InputChain)
            self.TheEventManager.AttachOutputTreeToVariables(self.OutTree)
            self.TheEventManager.GetTheCutDictionary() = CutDictionary

        def PerformSkim(self):
            print("Processing Skim...")
            for i in tqdm(range(self.InputChain.GetEntries())):
                self.InputChain.GetEntry(i)
                self.pileup_mc.Fill(self.TheEventManager.GetInputManager().GetInputDictionary["nTruePU"])
                
                if(not self.TheEventManager.IsGoodEvent()) continue
                #translate the input to output.
                self.TheEventManager.TranslateInputToOutput()

                #handle the staging
                #first event. Move current up to staged
                if(i == 0):
                    self.TheEventManager.GetTheOutputManager().GetStagedOutputDictionary() = self.TheEventManager.GetTheOutputManager().GetCurrentOutputDictionary()
                #duplicate event. Decide what to do about that.
                else if(self.TheEventManager.GetTheOutputManager().GetCurrentOutputDictionary()["evt"] == self.TheEventManager.GetTheOutputManager().GetStagedOutputDictionary["evt"]):
                    #TODO: Implement more complete priority scheme, for now this will do
                    #if the new pt_1 is greater, move the current up to staged
                    # or if the new pt_1 is greater than the old pt_1 minus a bit and the 
                    #pt_2 is greater than the old
                    #move the urrent 
                    if(self.PrioritySceme == "normal"):
                        if(self.EventManager.GetTheOutputManager().GetCurrentOutputDictionary["pt_1"] > self.EventManager.GetTheOutputManager.GetStagedOutputDictionary["pt_1"]):
                            self.TheEventManager.GetTheOutputManager().GetStagedOutputDictionary() = self.TheEventManager.GetTheOutputManager().GetCurrentOutputDictionary()
                        
                        if(self.EventManager.GetTheOutputManager().GetCurrentOutputDictionary["pt_1"] > self.EventManager.GetTheOutputManager.GetStagedOutputDictionary["pt_1"] - 0.00001
                           and self.EventManager.GetTheOutputManager().GetCurrentOutputDictionary["pt_2"] > self.EventManager.GetTheOutputManager.GetStagedOutputDictionary["pt_2"]):
                            self.TheEventManager.GetTheOutputManager().GetStagedOutputDictionary() = self.TheEventManager.GetTheOutputManager().GetCurrentOutputDictionary()
                #no similar event to compare to.
                #fill the staged event and move the current up to staged
                else:
                    self.OutTree.Fill()
                    self.TheEventManager.GetTheOutputManager().GetStagedOutputDictionary() = self.TheEventManager.GetTheOutputManager().GetCurrentOutputDictionary()
            #fill the last event we have staged
            self.OutTree.Fill()

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
    JesterworksImplementation.PrepEventManager()
    JesterworksImplementation.PerformSkim()
