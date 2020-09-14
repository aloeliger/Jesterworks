#!/usr/bin/env python
import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import ROOT
from TES import GetCorrectedMetVector

def CalculateEES_E_UP(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if not(theChain.gen_match_2 == 1 or theChain.gen_match_2 == 3):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 + 0.010)

    theBranch.BranchValue[0] = correctedTauVector.E()

def CalculateEES_E_DOWN(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if not(theChain.gen_match_2 == 1 or theChain.gen_match_2 == 3):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 - 0.010)
         
    theBranch.BranchValue[0] = correctedTauVector.E()

def CalculateEES_Pt_UP(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if not(theChain.gen_match_2 == 1 or theChain.gen_match_2 == 3):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 + 0.010)

    theBranch.BranchValue[0] = correctedTauVector.Pt()

def CalculateEES_Pt_DOWN(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if not(theChain.gen_match_2 == 1 or theChain.gen_match_2 == 3):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 - 0.010)

    theBranch.BranchValue[0] = correctedTauVector.Pt()

def CalculateEES_MET_UP(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if not(theChain.gen_match_2 == 1 or theChain.gen_match_2 == 3):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 + 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)

    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CalculateEES_MET_DOWN(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if not(theChain.gen_match_2 == 1 or theChain.gen_match_2 == 3):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 - 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)

    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CalculateEES_METPhi_UP(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if not(theChain.gen_match_2 == 1 or theChain.gen_match_2 == 3):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 + 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)

    theBranch.BranchValue[0] = correctedMETVector.Phi()

def CalculateEES_METPhi_DOWN(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if not(theChain.gen_match_2 == 1 or theChain.gen_match_2 == 3):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 - 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)

    theBranch.BranchValue[0] = correctedMETVector.Phi()

def CalculateMES_E_UP(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if not(theChain.gen_match_2 == 2 or theChain.gen_match_2 == 4):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 + 0.010)

    theBranch.BranchValue[0] = correctedTauVector.E()

def CalculateMES_E_DOWN(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if not(theChain.gen_match_2 == 2 or theChain.gen_match_2 == 4):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 - 0.010)

    theBranch.BranchValue[0] = correctedTauVector.E()

def CalculateMES_Pt_UP(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if not(theChain.gen_match_2 == 2 or theChain.gen_match_2 == 4):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 + 0.010)

    theBranch.BranchValue[0] = correctedTauVector.Pt()

def CalculateMES_Pt_DOWN(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if not(theChain.gen_match_2 == 2 or theChain.gen_match_2 == 4):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 - 0.010)

    theBranch.BranchValue[0] = correctedTauVector.Pt()

def CalculateMES_MET_UP(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if not(theChain.gen_match_2 == 2 or theChain.gen_match_2 == 4):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 + 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)

    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CalculateMES_MET_DOWN(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if not(theChain.gen_match_2 == 2 or theChain.gen_match_2 == 4):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 - 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)

    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CalculateMES_METPhi_UP(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if not(theChain.gen_match_2 == 2 or theChain.gen_match_2 == 4):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 + 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)

    theBranch.BranchValue[0] = correctedMETVector.Phi()

def CalculateMES_METPhi_DOWN(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if not(theChain.gen_match_2 == 2 or theChain.gen_match_2 == 4):
        correctedTauVector = tauVector
    else:
        correctedTauVector = tauVector * (1.0 - 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)

    theBranch.BranchValue[0] = correctedMETVector.Phi()

EES_E_UP_Branch = Branch.UserBranch()
EES_E_UP_Branch.Name = "EES_E_UP"
EES_E_UP_Branch.CalculateValue = CalculateEES_E_UP

EES_E_DOWN_Branch = Branch.UserBranch()
EES_E_DOWN_Branch.Name = "EES_E_DOWN"
EES_E_DOWN_Branch.CalculateValue = CalculateEES_E_DOWN

EES_Pt_UP_Branch = Branch.UserBranch()
EES_Pt_UP_Branch.Name = "EES_Pt_UP"
EES_Pt_UP_Branch.CalculateValue = CalculateEES_Pt_UP

EES_Pt_DOWN_Branch = Branch.UserBranch()
EES_Pt_DOWN_Branch.Name = "EES_Pt_DOWN"
EES_Pt_DOWN_Branch.CalculateValue = CalculateEES_Pt_DOWN

EES_MET_UP_Branch = Branch.UserBranch()
EES_MET_UP_Branch.Name = "EES_MET_UP"
EES_MET_UP_Branch.CalculateValue = CalculateEES_MET_UP

EES_MET_DOWN_Branch = Branch.UserBranch()
EES_MET_DOWN_Branch.Name = "EES_MET_DOWN"
EES_MET_DOWN_Branch.CalculateValue = CalculateEES_MET_DOWN

EES_METPhi_UP_Branch = Branch.UserBranch()
EES_METPhi_UP_Branch.Name = "EES_METPhi_UP"
EES_METPhi_UP_Branch.CalculateValue = CalculateEES_METPhi_UP

EES_METPhi_DOWN_Branch = Branch.UserBranch()
EES_METPhi_DOWN_Branch.Name = "EES_METPhi_DOWN"
EES_METPhi_DOWN_Branch.CalculateValue = CalculateEES_METPhi_DOWN

MES_E_UP_Branch = Branch.UserBranch()
MES_E_UP_Branch.Name = "MES_E_UP"
MES_E_UP_Branch.CalculateValue = CalculateMES_E_UP

MES_E_DOWN_Branch = Branch.UserBranch()
MES_E_DOWN_Branch.Name = "MES_E_DOWN"
MES_E_DOWN_Branch.CalculateValue = CalculateMES_E_DOWN

MES_Pt_UP_Branch = Branch.UserBranch()
MES_Pt_UP_Branch.Name = "MES_Pt_UP"
MES_Pt_UP_Branch.CalculateValue = CalculateMES_Pt_UP

MES_Pt_DOWN_Branch = Branch.UserBranch()
MES_Pt_DOWN_Branch.Name = "MES_Pt_DOWN"
MES_Pt_DOWN_Branch.CalculateValue = CalculateMES_Pt_DOWN

MES_MET_UP_Branch = Branch.UserBranch()
MES_MET_UP_Branch.Name = "MES_MET_UP"
MES_MET_UP_Branch.CalculateValue = CalculateMES_MET_UP

MES_MET_DOWN_Branch = Branch.UserBranch()
MES_MET_DOWN_Branch.Name = "MES_MET_DOWN"
MES_MET_DOWN_Branch.CalculateValue = CalculateMES_MET_DOWN

MES_METPhi_UP_Branch = Branch.UserBranch()
MES_METPhi_UP_Branch.Name = "MES_METPhi_UP"
MES_METPhi_UP_Branch.CalculateValue = CalculateMES_METPhi_UP

MES_METPhi_DOWN_Branch = Branch.UserBranch()
MES_METPhi_DOWN_Branch.Name = "MES_METPhi_DOWN"
MES_METPhi_DOWN_Branch.CalculateValue = CalculateMES_METPhi_DOWN
