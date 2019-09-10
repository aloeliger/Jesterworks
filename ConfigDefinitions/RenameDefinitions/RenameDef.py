#a quick class to define and perform renaming of branches on the chain
import ROOT

class RenameDictionary():
    def __init__(self):
        self.Renames={}
    def PerformTheRenaming(self,TheChain):
        for OriginalBranchName in self.Renames:
            TheBranch = TheChain.GetBranch(OriginalBranchName)
            if TheBranch != None:
                TheBranch.SetNameTitle(self.Renames[OriginalBranchName],self.Renames[OriginalBranchName])
