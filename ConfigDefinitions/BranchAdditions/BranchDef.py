#Define classes used for adding user defined branches to the chain
from tqdm import tqdm
from array import array
import ROOT

class UserBranch():
    def __init__(self):
        self.Name = ""
        self.BranchValue= array('f',[0.])
        self.CalculateValue = self.DefaultBranchCalcFunction
    def PrepareUserBranch(self,TheChain):
        self.Branch = TheChain.Branch(self.Name,self.BranchValue,self.Name+"/F")        
    def FillUserBranch(self):
        self.Branch.Fill()
    def DefaultBranchCalcFunction(self,TheChain):
        raise RuntimeError("Branch: "+self.Name+" does not have a defined way to calculate it's value!")

class UserBranchCollection():
    def __init__(self):
        self.UserBranches=[]
    def PrepCollection(self,TheChain):
        for DefinedBranch in self.UserBranches:
            DefinedBranch.PrepareUserBranch(TheChain)
    def AddBranches(self,TheChain):
        for i in range(TheChain.GetEntries()):
            TheChain.GetEntry(i)
            for DefinedBranch in self.UserBranches:
                DefinedBranch.CalculateValue(DefinedBranch,TheChain)
                DefinedBranch.FillUserBranch()
                #DefinedBranch.Branch.Print()
    
