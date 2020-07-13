import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import ROOT

def CalculateHiggsMass(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    metVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)

    theBranch.BranchValue[0] = (muVector+tauVector+metVector).M()

HiggsMassBranch = Branch.UserBranch()
HiggsMassBranch.Name = "HiggsMass"
HiggsMassBranch.CalculateValue = CalculateHiggsMass
