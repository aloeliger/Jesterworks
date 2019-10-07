# a class used for correcting in place branches of the chain.
#okay, how do we do this?
# need the name of the branch to be corrected
# a variable we're goin to store our corrected value in
#A function we can overwrite to retrieve the new value of the variable
from array import array

class BranchCorrections():
    def __init__(self):
        self.CorrectionList={}
        self.CorrectionBranches={}
        self.CorrectionValues={}
    #for creating all the arrays needed for values in the branches
    def CreateArrays(self):
        for Key in CorrectionList:
            self.CorrectionValues[Key] = array('f',[0.])
    # This will do the branch manipulation and copying to end up with 
    #a copy of the old chain but with empty branches for correcting
    def PrepOldAndNewChains(self,TheChain):        
        for Key in CorrectionList:
            TheChain.GetBranch(Key).SetBranchStatus(0)            
        self.NewChain = TheChain.Clone()    
        for Key in CorrectionList:
            TheChain.GetBranch(Key).SetBranchStatus(1)
            self.CorrectionBranches[Key] = self.NewChain.Branch(Key,self.CorrectionValues[Key],Key+"/F")            
    # function for actually looping the chain and filling values.
    def PerformAllCorrections(self,TheChain):
        for i in range(TheChain.GetEntries()):
            TheChain.GetEntry(i)
            for Key in self.CorrectionList:
                self.CorrectionValues[Key][0] = self.CorrectionList[Key](TheChain)
                self.CorrectionBranches[Key].Fill()
    #master handle function for use in the main script. Runs all steps.
    def GetCorrectedTree(self,TheChain):
        self.CreateArrays()
        self.PrepOldAndNewChains(TheChain)
        self.PerformAllCorrections(TheChain)
        return self.NewChain
