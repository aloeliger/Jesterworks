import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import ROOT

def CalculateVisibleMass(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)

    theBranch.BranchValue[0] = (muVector+tauVector).M()

VisibleMassBranch = Branch.UserBranch()
VisibleMassBranch.Name = "m_vis"
VisibleMassBranch.CalculateValue = CalculateVisibleMass
