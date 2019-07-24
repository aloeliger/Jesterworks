import ROOT
import sys
from Jesterworks import Jesterworks
import math

def HTTSelectionCuts(TheEvent, SampleName = ""):
    isGoodEvent = True

    MuonVector = ROOT.TLorentzVector()
    TauVector = ROOT.TLorentzVector()
    METVector = ROOT.TLorentzVector()

    MuonVector.SetPtEtaPhiM(TheEvent.pt_1,TheEvent.eta_1,TheEvent.phi_1,TheEvent.m_1)
    TauVector.SetPtEtaPhiM(TheEvent.pt_2,TheEvent.eta_2,TheEvent.phi_2,TheEvent.m_2)
    METVector.SetPtEtaPhiM(TheEvent.met,0.0,TheEvent.metphi,0.0)

    
    if(abs(TheEvent.eta_1) > 2.1 or abs(TheEvent.eta_2) > 2.3):
        isGoodEvent = False
    if(TheEvent.pt_1 < 20.0 or TheEvent.pt_2 < 20.0):
        isGoodEvent = False

    if(TheEvent.flag_goodVertices
       or TheEvent.flag_globalSuperTightHalo2016
       or TheEvent.flag_eeBadSc
       or SampleName == "data_ovs" and TheEvent.flag_eeBadSc
       or TheEvent.flag_ecalBadCalib
       or TheEvent.flag_badMuons
       or TheEvent.flag_duplicateMuons
       or TheEvent.flag_HBHENoiseIso
       or TheEvent.flag_HBHENoise
       or TheEvent.flag_EcalDeadCellTriggerPrimitive
       or TheEvent.flag_BadPFMuon
       or TheEvent.flag_BadChargedCandidate):
        isGoodEvent = False
        
    Trigger22 = (TheEvent.pt_1 >23.0 and abs(TheEvent.eta_1)<2.1 
                 and ((TheEvent.passMu22eta2p1 and TheEvent.matchMu22eta2p1_1 and TheEvent.filterMu22eta2p1_1) 
                      or (TheEvent.passTkMu22eta2p1 and TheEvent.matchTkMu22eta2p1_1 and TheEvent.filterTkMu22eta2p1_1)))

    Trigger1920 = (TheEvent.pt_1 > 20.0 and TheEvent.pt_2 > 21.0 
                   and ((TheEvent.passMu19Tau20 and TheEvent.matchMu19Tau20_1 and TheEvent.matchMu19Tau20_2 and TheEvent.filterMu19Tau20_1 and TheEvent.filterMu19Tau20_2) 
                        or (TheEvent.passMu19Tau20SingleL1 and TheEvent.matchMu19Tau20SingleL1_1 and TheEvent.matchMu19Tau20SingleL1_2 and TheEvent.filterMu19Tau20SingleL1_1 and TheEvent.filterMu19Tau20SingleL1_2)))

    if(not (Trigger22 or Trigger1920)):
        isGoodEvent = False
        
    #avoid overlap with FFs
    if(TheEvent.gen_match_2 == 6):
        isGoodEvent = False
    
    if(not TheEvent.againstElectronVLooseMVA6_2 or not TheEvent.againstMuonTight3_2):
        isGoodEvent = False

    if(TheEvent.nbtag>0):
        isGoodEvent = False
        
    if(TheEvent.q_1 * TheEvent.q_2 > 0):
        isGoodEvent = False
        
    signalRegion = (TheEvent.byTightIsolationMVArun2v2DBoldDMwLT_2 and TheEvent.iso_1 < 0.15)

    if(not signalRegion):
        isGoodEvent = False
    
    return isGoodEvent

def TrivialPriority(NewEventDictionary,OldEventDictionary):
    return True

if __name__ == "__main__":
    ConfFile  =sys.argv[1]
    TheSkim = Jesterworks(ConfFile,HTTSelectionCuts,TrivialPriority)
    TheSkim.CreateListOfFilesToRunOn()
    TheSkim.Run()
