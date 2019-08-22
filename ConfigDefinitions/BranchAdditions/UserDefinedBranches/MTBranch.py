#Create and attach a calculation of transverse mass to the chain
import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import math

def CalculateMT(TheBranch,TheChain):
    TheBranch.BranchValue[0] = math.sqrt(2.0*TheChain.pt_1*TheChain.met*(1.0-math.cos(abs(TheChain.phi_1-TheChain.metphi))))

MTBranch = Branch.UserBranch()
MTBranch.Name = "MT"
MTBranch.CalculateValue = CalculateMT
