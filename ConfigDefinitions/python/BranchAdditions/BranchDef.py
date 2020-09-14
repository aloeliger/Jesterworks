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
        fillStatus = self.Branch.Fill()
        """
        if fillStatus == -1:
            print "entries after bad fill: "+str(self.Branch.GetEntries())
            print("Branch val: "+str(self.BranchValue[0]))
            print ROOT.gDirectory.pwd()
            self.Branch.Print()
            #print("Retrying fill...")
            #self.Branch.Fill()
            #print "Entries after retried fill: "+str(self.Branch.GetEntries())
            raise RuntimeError
        """
        return fillStatus
    def DefaultBranchCalcFunction(self,TheBranch,TheChain):
        raise RuntimeError("Branch: "+self.Name+" does not have a defined way to calculate it's value!")

class UserBranchCollection():
    def __init__(self):
        self.UserBranches=[]
    def PrepCollection(self,TheChain):
        for DefinedBranch in self.UserBranches:
            DefinedBranch.PrepareUserBranch(TheChain)
    def AddBranches(self,TheChain):
        for i in range(TheChain.GetEntries()):
            #print(i)
            TheChain.GetEntry(i)
            for DefinedBranch in self.UserBranches:                
                DefinedBranch.CalculateValue(DefinedBranch,TheChain)                
                DefinedBranch.FillUserBranch()                
                #DefinedBranch.Branch.Print()
    
