import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import ROOT

def CalculateFiducial(theBranch,theChain):
    theBranch.BranchValue[0] = 0.0    

FiducialBranch = Branch.UserBranch()
FiducialBranch.Name = "is_Fiducial"
FiducialBranch.CalculateValue = CalculateFiducial
