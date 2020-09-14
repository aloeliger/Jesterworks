import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import math
import ROOT

def CalculateFiducial(theBranch,theChain):
    #isFiducial = (abs(theChain.gentau1_eta)<2.5
    #              and abs(theChain.gentau2_eta)<2.5
    #              and abs(theChain.gentau1_pt)>25.0
    #              and abs(theChain.gentau2_pt)>25.0)
    genMT = math.sqrt(2.0*theChain.gen_mu_pt*theChain.gen_met_pt*(1.0-math.cos(abs(theChain.gen_mu_phi-theChain.gen_met_phi))))
    isFiducial = (
        theChain.gen_tauh_pt > 30
        and abs(theChain.gen_tauh_eta ) < 2.3
        and theChain.gen_mu_pt > 20
        and abs(theChain.gen_mu_eta) < 2.1
        and theChain.HTTgenfinalstate == 3
        and genMT < 50
        )
    if isFiducial:
        theBranch.BranchValue[0] = 1.0
    else:
        theBranch.BranchValue[0] = 0.0    

FiducialBranch = Branch.UserBranch()
FiducialBranch.Name = "is_Fiducial"
FiducialBranch.CalculateValue = CalculateFiducial
