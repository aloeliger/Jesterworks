import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import ROOT
from TES import GetCorrectedMetVector

def CreateMuonES_E_UP(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)

    if(muVector.Eta() >= -2.4 and muVector.Eta() < -2.1):
        correctedMuVector = muVector * (1.0 + 0.027)
    elif(muVector.Eta()>=-2.1 and muVector.Eta() < -1.2):
        correctedMuVector = muVector * (1.0 + 0.009)
    elif(muVector.Eta() >= -1.2 and muVector.Eta() < 1.2):
        correctedMuVector = muVector * (1.0 + 0.004)
    elif(muVector.Eta() >= 1.2 and muVector.Eta() < 2.1):
        correctedMuVector = muVector * (1.0 + 0.009)
    elif(muVector.eta() >= 2.1 and muVector.Eta() < 2.4):
        correctedMuVector = muVector * (1.0 + 0.017)
    
    theBranch.BranchValue[0] = correctedMuVector.E()

def CreateMuonES_E_DOWN(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)

    if(muVector.Eta() >= -2.4 and muVector.Eta() < -2.1):
        correctedMuVector = muVector * (1.0 - 0.027)
    elif(muVector.Eta()>=-2.1 and muVector.Eta() < -1.2):
        correctedMuVector = muVector * (1.0 - 0.009)
    elif(muVector.Eta() >= -1.2 and muVector.Eta() < 1.2):
        correctedMuVector = muVector * (1.0 - 0.004)
    elif(muVector.Eta() >= 1.2 and muVector.Eta() < 2.1):
        correctedMuVector = muVector * (1.0 - 0.009)
    elif(muVector.eta() >= 2.1 and muVector.Eta() < 2.4):
        correctedMuVector = muVector * (1.0 - 0.017)
    
    theBranch.BranchValue[0] = correctedMuVector.E()

def CreateMuonES_Pt_UP(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)

    if(muVector.Eta() >= -2.4 and muVector.Eta() < -2.1):
        correctedMuVector = muVector * (1.0 + 0.027)
    elif(muVector.Eta()>=-2.1 and muVector.Eta() < -1.2):
        correctedMuVector = muVector * (1.0 + 0.009)
    elif(muVector.Eta() >= -1.2 and muVector.Eta() < 1.2):
        correctedMuVector = muVector * (1.0 + 0.004)
    elif(muVector.Eta() >= 1.2 and muVector.Eta() < 2.1):
        correctedMuVector = muVector * (1.0 + 0.009)
    elif(muVector.eta() >= 2.1 and muVector.Eta() < 2.4):
        correctedMuVector = muVector * (1.0 + 0.017)
    
    theBranch.BranchValue[0] = correctedMuVector.Pt()

def CreateMuonES_Pt_DOWN(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)

    if(muVector.Eta() >= -2.4 and muVector.Eta() < -2.1):
        correctedMuVector = muVector * (1.0 - 0.027)
    elif(muVector.Eta()>=-2.1 and muVector.Eta() < -1.2):
        correctedMuVector = muVector * (1.0 - 0.009)
    elif(muVector.Eta() >= -1.2 and muVector.Eta() < 1.2):
        correctedMuVector = muVector * (1.0 - 0.004)
    elif(muVector.Eta() >= 1.2 and muVector.Eta() < 2.1):
        correctedMuVector = muVector * (1.0 - 0.009)
    elif(muVector.eta() >= 2.1 and muVector.Eta() < 2.4):
        correctedMuVector = muVector * (1.0 - 0.017)
    
    theBranch.BranchValue[0] = correctedMuVector.Pt()

def CreateMuonES_MET_UP(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)
    metVector = ROOT.TLorentzVector()

    if(muVector.Eta() >= -2.4 and muVector.Eta() < -2.1):
        correctedMuVector = muVector * (1.0 + 0.027)
    elif(muVector.Eta()>=-2.1 and muVector.Eta() < -1.2):
        correctedMuVector = muVector * (1.0 + 0.009)
    elif(muVector.Eta() >= -1.2 and muVector.Eta() < 1.2):
        correctedMuVector = muVector * (1.0 + 0.004)
    elif(muVector.Eta() >= 1.2 and muVector.Eta() < 2.1):
        correctedMuVector = muVector * (1.0 + 0.009)
    elif(muVector.eta() >= 2.1 and muVector.Eta() < 2.4):
        correctedMuVector = muVector * (1.0 + 0.017)
    correctedMETVector = GetCorrectedMetVector(muVector,correctedMuVector,metVector)
    
    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CreateMuonES_MET_DOWN(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)
    metVector = ROOT.TLorentzVector()

    if(muVector.Eta() >= -2.4 and muVector.Eta() < -2.1):
        correctedMuVector = muVector * (1.0 - 0.027)
    elif(muVector.Eta()>=-2.1 and muVector.Eta() < -1.2):
        correctedMuVector = muVector * (1.0 - 0.009)
    elif(muVector.Eta() >= -1.2 and muVector.Eta() < 1.2):
        correctedMuVector = muVector * (1.0 - 0.004)
    elif(muVector.Eta() >= 1.2 and muVector.Eta() < 2.1):
        correctedMuVector = muVector * (1.0 - 0.009)
    elif(muVector.eta() >= 2.1 and muVector.Eta() < 2.4):
        correctedMuVector = muVector * (1.0 - 0.017)
    correctedMETVector = GetCorrectedMetVector(muVector,correctedMuVector,metVector)
    
    theBranch.BranchValue[0] = correctedMETVector.Pt()

def CreateMuonES_METPhi_UP(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)
    metVector = ROOT.TLorentzVector()

    if(muVector.Eta() >= -2.4 and muVector.Eta() < -2.1):
        correctedMuVector = muVector * (1.0 + 0.027)
    elif(muVector.Eta()>=-2.1 and muVector.Eta() < -1.2):
        correctedMuVector = muVector * (1.0 + 0.009)
    elif(muVector.Eta() >= -1.2 and muVector.Eta() < 1.2):
        correctedMuVector = muVector * (1.0 + 0.004)
    elif(muVector.Eta() >= 1.2 and muVector.Eta() < 2.1):
        correctedMuVector = muVector * (1.0 + 0.009)
    elif(muVector.eta() >= 2.1 and muVector.Eta() < 2.4):
        correctedMuVector = muVector * (1.0 + 0.017)
    correctedMETVector = GetCorrectedMetVector(muVector,correctedMuVector,metVector)
    
    theBranch.BranchValue[0] = correctedMETVector.Phi()

def CreateMuonES_METPhi_DOWN(theBranch,theChain):
    muVector = ROOT.TLorentzVector()
    muVector.SetPtEtaPhiM(theChain.pt_1,theChain.eta_1,theChain.phi_1,theChain.m_1)
    metVector = ROOT.TLorentzVector()

    if(muVector.Eta() >= -2.4 and muVector.Eta() < -2.1):
        correctedMuVector = muVector * (1.0 - 0.027)
    elif(muVector.Eta()>=-2.1 and muVector.Eta() < -1.2):
        correctedMuVector = muVector * (1.0 - 0.009)
    elif(muVector.Eta() >= -1.2 and muVector.Eta() < 1.2):
        correctedMuVector = muVector * (1.0 - 0.004)
    elif(muVector.Eta() >= 1.2 and muVector.Eta() < 2.1):
        correctedMuVector = muVector * (1.0 - 0.009)
    elif(muVector.eta() >= 2.1 and muVector.Eta() < 2.4):
        correctedMuVector = muVector * (1.0 - 0.017)
    correctedMETVector = GetCorrectedMetVector(muVector,correctedMuVector,metVector)
    
    theBranch.BranchValue[0] = correctedMETVector.Phi()

muonES_E_UP_Branch = Branch.UserBranch()
muonES_E_UP_Branch.Name = "muonES_E_UP"
muonES_E_UP_Branch.CalculateValue = CreateMuonES_E_UP

muonES_E_DOWN_Branch = Branch.UserBranch()
muonES_E_DOWN_Branch.Name = "muonES_E_DOWN"
muonES_E_DOWN_Branch.CalculateValue = CreateMuonES_E_DOWN

muonES_Pt_UP_Branch = Branch.UserBranch()
muonES_Pt_UP_Branch.Name = "muonES_Pt_UP"
muonES_Pt_UP_Branch.CalculateValue = CreateMuonES_Pt_UP

muonES_Pt_DOWN_Branch = Branch.UserBranch()
muonES_Pt_DOWN_Branch.Name = "muonES_Pt_DOWN"
muonES_Pt_DOWN_Branch.CalculateValue = CreateMuonES_Pt_DOWN

muonES_MET_UP_Branch = Branch.UserBranch()
muonES_MET_UP_Branch.Name = "muonES_MET_UP"
muonES_MET_UP_Branch.CalculateValue = CreateMuonES_MET_UP

muonES_MET_DOWN_Branch = Branch.UserBranch()
muonES_MET_DOWN_Branch.Name = "muonES_MET_DOWN"
muonES_MET_DOWN_Branch.CalculateValue = CreateMuonES_MET_DOWN

muonES_METPhi_UP_Branch = Branch.UserBranch()
muonES_METPhi_UP_Branch.Name = "muonES_METPhi_UP"
muonES_METPhi_UP_Branch.CalculateValue = CreateMuonES_METPhi_UP

muonES_METPhi_DOWN_Branch = Branch.UserBranch()
muonES_METPhi_DOWN_Branch.Name = "muonES_METPhi_DOWN"
muonES_METPhi_DOWN_Branch.CalculateValue = CreateMuonES_METPhi_DOWN
