import ROOT
from array import array

class InputManager:
    def __init__(self):
        self.InputDictionary = {}

    def CreateDictionaryBranchAndAttach(self,TheChain,Name):
        self.InputDictionary[Name] = array('f', [0])
        TheChain.SetBranchAddress(Name,self.InputDictionary[Name],Name+'/F')
    
    def GetInputDictionary(self):
        return self.InputDictionary
