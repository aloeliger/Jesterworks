import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import ROOT

def CalculateFiducial(theBranch,theChain):
    isFiducial = (abs(theChain.gentau1_eta)<2.5
                  and abs(theChain.gentau2_eta)<2.5
                  and abs(theChain.gentau1_pt)>25.0
                  and abs(theChain.gentau2_pt)>25.0)
    if isFiducial:
        theBranch.BranchValue[0] = 1.0
    else:
        theBranch.BranchValue[0] = 0.0    

FiducialBranch = Branch.UserBranch()
FiducialBranch.Name = "is_Fiducial"
FiducialBranch.CalculateValue = CalculateFiducial
