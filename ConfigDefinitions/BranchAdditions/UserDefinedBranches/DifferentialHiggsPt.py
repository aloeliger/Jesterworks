import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import ROOT
import math
import os

currentLocation = os.path.dirname(__file__)

def CalculateDifferentialHiggsPt(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    tauVector = ROOT.TLorentzVector()
    metVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)

    higgsVector = (muVector+tauVector+metVector)
    correctedPTH = higgsVector.Pt()*theBranch.correctionFunction.Eval(higgsVector.Pt())
    if correctedPTH < 0:
        correctedPTH = 0.5
    theBranch.BranchValue[0] = correctedPTH

differentialHiggsPtBranch = Branch.UserBranch()
differentialHiggsPtBranch.Name = "HiggsPt_Differential"
differentialHiggsPtBranch.correctionFile = ROOT.TFile(os.path.join(currentLocation,"RootFiles/pthcorrection_et.root"))
differentialHiggsPtBranch.correctionFunction = differentialHiggsPtBranch.correctionFile.Get("pth_correction")
differentialHiggsPtBranch.CalculateValue = CalculateDifferentialHiggsPt
