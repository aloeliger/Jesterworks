import ROOT
from array import array

class OutputManager:
    def __init__(self):
        self.StagedOutputDictionary = {}
        self.CurrentOutputDictionary = {}

    def CreateDictionaryBranchAndAttach(self,TheTree,Name):
        self.StagedOutputDictionary[Name] = array('f',[0])
        self.CurrentOutputDictionary[Name] = array('f',[0])
        TheTree.Branch(Name,self.StagedOutputDictionary[Name],Name+'/F')

    def GetCurrentOutputDictionary(self):
        return self.CurrentOutputDictionary

    def GetStagedOutputDictionary(self):
        return self.StagedOutputDictionary
