#configuration for creating met UES Up Branches

import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import ROOT

def CalculateMET_UESUp(TheBranch,TheChain):
    pass
    

Met_UESUp_Branch = Branch.UserBranch()
Met_UESUp_Branch.Name = "met_UESUp"
Met_UESUp_Branch.CalculateMET_UESUp
