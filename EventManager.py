import ROOT
from array import array

from InputManager import InputManager
from OutputManager import OutputManager

class EventManager:
    def __init__(self):
        self.InputBranchNames = []
        self.OutputBranchNames = []
        self.TranslationDictionary = {}
        self.TheInputManager = InputManager()
        self.TheOutputManager = OutputManager()
        self.TheCutDictionary = {}

    def GetInputBranchNameList(self):
        return self.InputBranchNames

    def GetOutputBranchNamesList(self):
        return self.OutputBranchNames

    def GetTranslationDictionary(self):
        return self.TranslationDictionary

    def GetTheInputManager(self):
        return self.TheInputManager
    
    def GetTheOutputManager(self):
        return self.TheOutputManager

    def GetTheCutDictionary(self):
        return self.TheCutDictionary

    def TranslateInputToOutput(self):
        for InputVar in TranslationDictionary:
            self.GetTheOutputManager().GetCurrentOutputDictionary()[self.TranslationDictionary[InputVar]][0] = self.GetTheInputManager().GetInputDictionary()[InputVar][0]

    def AttachInputChainToVariables(self,TheChain):
        for Name in self.GetInputBranchNameList():
            self.GetTheInputManager().CreateDictionaryBranchAndAttach(TheChain,Name)

    def AttachOutputTreeToVariables(self,TheTree):
        for Name in self.GetOutputBranchNameList():
            self.GetTheOutputManager().CreateDictionaryBranchAndAttach(TheTree,Name)
    
    def IsGoodEvent(self):
        EventValid = True
        for Var in TheCutDictionary.keys():
            if(not VarPassesCut(self.GetTheInputManager().GetInputDictionary()[Var][0],TheCutDictionary[Var])):
                EventValid = False
        return EventValid

    def VarPassesCut(self,Var,CutString):
        CutOp = CutString[:1]
        CutVal = CutString[1:]
        if(CutOp == ">" and Var > CutVal):            
            return True
        if(CutOp == "<" and Var < CutVal):
            return True
        if(CutOp == "=" and Var == CutVal):
            return True
        if(CutOP == "!" and not Var):
            return True
        if(CutOP == "Y" and Var):
            return True
        if(CutOP == "O"):
            OtherVar = self.GetTheInputManager.GetInputDictionary()[CutVal][0]
            if(Var or OtherVar):
                return True
        if(CutOP == "A"):
            OtherVar = self.GetTheInputManager.GetInputDictionary()[CutVal][0]
            if(Var and OtherVar):
                return True
        return False
