import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import math
import ROOT

def CalculateFiducial(theBranch,theChain):
    isFiducial = (abs(theChain.gentau1_eta)<2.5
                  and abs(theChain.gentau2_eta)<2.5
                  and abs(theChain.gentau1_pt)>25.0
                  and abs(theChain.gentau2_pt)>25.0)
    #genMT = math.sqrt(2.0*theChain.dressedMuon_pt*theChain.genMetPt*(1.0-math.cos(abs(theChain.mGenPhi-theChain.genMetPhi))))
    #isFiducial = (
    #    theChain.tGenJetPt > 30
    #    and abs(theChain.tGenJetEta ) < 2.3
    #    and theChain.dressedMuon_pt > 20
    #    and abs(theChain.mGenEta) < 2.1
    #    and theChain.HTTgenfinalstate == 3
    #    and genMT < 50
    #    )
    if isFiducial:
        theBranch.BranchValue[0] = 1.0
    else:
        theBranch.BranchValue[0] = 0.0    

FiducialBranch = Branch.UserBranch()
FiducialBranch.Name = "is_Fiducial"
FiducialBranch.CalculateValue = CalculateFiducial
