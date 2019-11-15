#!/usr/bin/env python

import ConfigDefinitinos.BranchAdditions.BranchDef as Branch
import ROOT

def GetCorrectedMetVector(tauVector, correctedTauVector, metVector):
    transverseTauVector = ROOT.TLorentzVector()
    transverseTauVector.SetPtEtaPhiM(tauVector.Pt(),0.0,tauVector.Phi(),tauVector.M())
    correctedTransverseTauVector = ROOT.TLorentzVector()
    correctedTransverseTauVector.SetPtEtaPhiM(correctedTauVector.Pt(),0.0,correctedTauVector.Phi(),correctedTauVector.M())
    correctedMetVector = transverseTauVector-correctedTransverseTauVector + metVector
    return correctedMetVector

#2016 calculations
def CalculateTES_E_UP_2016(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.010)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.011)
    theBranch.BranchValue[0] = correctedTauVector.E()

def CalculateTES_E_DOWN_2016(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.010)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.011)
    theBranch.BranchValue[0] = correctedTauVector.E()

def CalculateTES_PT_UP_2016(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.010)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.011)
    theBranch.BranchValue[0] = correctedTauVector.Pt()

def CalculateTES_PT_DOWN_2016(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.010)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.011)
    theBranch.BranchValue[0] = correctedTauVector.Pt()

def CalculateTES_MET_UP_2016(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.010)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.011)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)
    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CalculateTES_MET_DOWN_2016(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.010)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.011)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)
    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CalculateTES_METPhi_UP_2016(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.010)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.011)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,)
    theBranch.BranchValue[0] = correctedMETVector.Phi()

def CalculateTES_METPhi_DOWN_2016(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.010)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.011)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,)
    theBranch.BranchValue[0] = correctedMETVector.Phi()

#2017 calculations
def CalculateTES_E_UP_2017(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.008)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.008)
        elif theChain.l2_decayMode == 10:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif the Chain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.010)
    theBranch.BranchValue[0] = correctedTauVector.E()

def CalculateTES_E_DOWN_2017(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.008)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.008)
        elif theChain.l2_decayMode == 10:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif the Chain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.010)
    theBranch.BranchValue[0] = correctedTauVector.E()

def CalculateTES_PT_UP_2017(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.008)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.008)
        elif theChain.l2_decayMode == 10:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif the Chain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.010)
    theBranch.BranchValue[0] = correctedTauVector.Pt()

def CalculateTES_PT_DOWN_2017(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.008)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.008)
        elif theChain.l2_decayMode == 10:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif the Chain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.010)
    theBranch.BranchValue[0] = correctedTauVector.Pt()

def CalculateTES_MET_UP_2017(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.008)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.008)
        elif theChain.l2_decayMode == 10:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif the Chain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)
    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CalculateTES_MET_DOWN_2017(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.008)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.008)
        elif theChain.l2_decayMode == 10:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif the Chain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)
    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CalculateTES_METPhi_UP_2017(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.008)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.008)
        elif theChain.l2_decayMode == 10:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif the Chain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)
    theBranch.BranchValue[0] = correctedMETVector.Phi()

def CalculateTES_METPhi_DOWN_2017(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOT.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.008)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.008)
        elif theChain.l2_decayMode == 10:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif the Chain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.010)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)
    theBranch.BranchValue[0] = correctedMETVector.Phi()

#2018 TES corrections
def CalculateTES_E_UP_2018(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.011)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.008)
    theBranch.BranchValue[0] = correctedTauVector.E()

def CalculateTES_E_DOWN_2018(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.011)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.008)
    theBranch.BranchValue[0] = correctedTauVector.E()

def CalculateTES_PT_UP_2018(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.011)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.008)
    theBranch.BranchValue[0] = correctedTauVector.Pt()

def CalculateTES_PT_DOWN_2018(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.gen_match_2 == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.011)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.008)
    theBranch.BranchValue[0] = correctedTauVector.Pt()

def CalculateTES_MET_UP_2018(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOt.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.011)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.008)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)
    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CalculateTES_MET_DOWN_2018(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOt.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.011)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.008)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)
    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CalculateTES_METPhi_UP_2018(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOt.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 + 0.011)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 + 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 + 0.008)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)
    theBranch.BranchValue[0] = correctedMETVector.Phi()

def CalculateTES_METPhi_DOWN_2018(theBranch,theChain):
    tauVector = ROOT.TLorentzVector()
    tauVector.SetPtEtaPhiM(theChain.pt_2,theChain.eta_2,theChain.phi_2,theChain.m_2)
    metVector = ROOt.TLorentzVector()
    metVector.SetPtEtaPhiM(theChain.met,0.0,theChain.metphi,0.0)
    if theChain.gen_match_2 != 5:
        correctedTauVector = tauVector
    elif theChain.l2_decaymode == 5:
        if theChain.l2_decayMode == 0:
            correctedTauVector = tauVector * (1.0 - 0.011)
        elif theChain.l2_decayMode == 1:
            correctedTauVector = tauVector * (1.0 - 0.009)
        elif theChain.l2_decayMode == 10 or theChain.l2_decayMode == 11:
            correctedTauVector = tauVector * (1.0 - 0.008)
    correctedMETVector = GetCorrectedMetVector(tauVector,correctedTauVector,metVector)
    theBranch.BranchValue[0] = correctedMETVector.Phi()

#2016 branches
TES_E_UP_2016Branch = Branch.UserBranch()
TES_E_UP_2016Branch.Name = "TES_E_UP"
TES_E_UP_2016Branch.CalculateValue = CalculateTES_E_UP_2016

TES_E_DOWN_2016Branch = Branch.UserBranch()
TES_E_DOWN_2016Branch.Name = "TES_E_DOWN"
TES_E_DOWN_2016Branch.CalculateValue = CalculateTES_E_DOWN_2016

TES_PT_UP_2016Branch = Branch.UserBranch()
TES_PT_UP_2016Branch.Name = "TES_Pt_UP"
TES_PT_UP_2016Branch.CalculateValue = CalculateTES_PT_UP_2016

TES_PT_DOWN_2016Branch = Branch.UserBranch()
TES_PT_DOWN_2016Branch.Name = "TES_Pt_DOWN"
TES_PT_DOWN_2016Branch.CalculateValue = CalculateTES_PT_DOWN_2016

TES_MET_UP_2016Branch = Branch.UserBranch()
TES_MET_UP_2016Branch.Name = "TES_MET_UP"
TES_MET_UP_2016Branch.CalculateValue = CalculateTES_MET_UP_2016

TES_MET_DOWN_2016Branch = Branch.UserBranch()
TES_MET_DOWN_2016Branch.Name = "TES_MET_DOWN"
TES_MET_DOWN_2016Branch.CalculateValue = CalculateTES_MET_DOWN_2016

TES_METPhi_UP_2016Branch = Branch.UserBranch()
TES_METPhi_UP_2016Branch.Name = "TES_METPhi_UP"
TES_METPhi_UP_2016Branch.CalculateValue = CalculateTES_METPhi_UP_2016

TES_METPhi_DOWN_2016Branch = Branch.UserBranch()
TES_METPhi_DOWN_2016Branch.Name = "TES_MET_DOWN"
TES_METPhi_DOWN_2016Branch.CalculateValue = CalculateTES_METPhi_DOWN_2016

#2017 branches
TES_E_UP_2017Branch = Branch.UserBranch()
TES_E_UP_2017Branch.Name = "TES_E_UP"
TES_E_UP_2017Branch.CalculateValue = CalculateTES_E_UP_2017

TES_E_DOWN_2017Branch = Branch.UserBranch()
TES_E_DOWN_2017Branch.Name = "TES_E_DOWN"
TES_E_DOWN_2017Branch.CalculateValue = CalculateTES_E_DOWN_2017

TES_PT_UP_2017Branch = Branch.UserBranch()
TES_PT_UP_2017Branch.Name = "TES_Pt_UP"
TES_PT_UP_2017Branch.CalculateValue = CalculateTES_PT_UP_2017

TES_PT_DOWN_2017Branch = Branch.UserBranch()
TES_PT_DOWN_2017Branch.Name = "TES_Pt_DOWN"
TES_PT_DOWN_2017Branch.CalculateValue = CalculateTES_PT_DOWN_2017

TES_MET_UP_2017Branch = Branch.UserBranch()
TES_MET_UP_2017Branch.Name = "TES_MET_UP"
TES_MET_UP_2017Branch.CalculateValue = CalculateTES_MET_UP_2017

TES_MET_DOWN_2017Branch = Branch.UserBranch()
TES_MET_DOWN_2017Branch.Name = "TES_MET_DOWN"
TES_MET_DOWN_2017Branch.CalculateValue = CalculateTES_MET_DOWN_2017

TES_METPhi_UP_2017Branch = Branch.UserBranch()
TES_METPhi_UP_2017Branch.Name = "TES_METPhi_UP"
TES_METPhi_UP_2017Branch.CalculateValue = CalculateTES_METPhi_UP_2017

TES_METPhi_DOWN_2017Branch = Branch.UserBranch()
TES_METPhi_DOWN_2017Branch.Name = "TES_MET_DOWN"
TES_METPhi_DOWN_2017Branch.CalculateValue = CalculateTES_METPhi_DOWN_2017

#2018 branches
TES_E_UP_2018Branch = Branch.UserBranch()
TES_E_UP_2018Branch.Name = "TES_E_UP"
TES_E_UP_2018Branch.CalculateValue = CalculateTES_E_UP_2018

TES_E_DOWN_2018Branch = Branch.UserBranch()
TES_E_DOWN_2018Branch.Name = "TES_E_DOWN"
TES_E_DOWN_2018Branch.CalculateValue = CalculateTES_E_DOWN_2018

TES_PT_UP_2018Branch = Branch.UserBranch()
TES_PT_UP_2018Branch.Name = "TES_Pt_UP"
TES_PT_UP_2018Branch.CalculateValue = CalculateTES_PT_UP_2018

TES_PT_DOWN_2018Branch = Branch.UserBranch()
TES_PT_DOWN_2018Branch.Name = "TES_Pt_DOWN"
TES_PT_DOWN_2018Branch.CalculateValue = CalculateTES_PT_DOWN_2018

TES_MET_UP_2018Branch = Branch.UserBranch()
TES_MET_UP_2018Branch.Name = "TES_MET_UP"
TES_MET_UP_2018Branch.CalculateValue = CalculateTES_MET_UP_2018

TES_MET_DOWN_2018Branch = Branch.UserBranch()
TES_MET_DOWN_2018Branch.Name = "TES_MET_DOWN"
TES_MET_DOWN_2018Branch.CalculateValue = CalculateTES_MET_DOWN_2018

TES_METPhi_UP_2018Branch = Branch.UserBranch()
TES_METPhi_UP_2018Branch.Name = "TES_METPhi_UP"
TES_METPhi_UP_2018Branch.CalculateValue = CalculateTES_METPhi_UP_2018

TES_METPhi_DOWN_2018Branch = Branch.UserBranch()
TES_METPhi_DOWN_2018Branch.Name = "TES_MET_DOWN"
TES_METPhi_DOWN_2018Branch.CalculateValue = CalculateTES_METPhi_DOWN_2018
