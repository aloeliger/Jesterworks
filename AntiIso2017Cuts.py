import ROOT
import sys
from Jesterworks import Jesterworks
import math
import argparse

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
        
    if(TheEvent.Flag_goodVertices       
       or TheEvent.Flag_globalSuperTightHalo2016Filter
       or TheEvent.Flag_HBHENoiseFilter
       or TheEvent.Flag_HBHENoiseIsoFilter
       or TheEvent.Flag_EcalDeadCellTriggerPrimitiveFilter
       or TheEvent.Flag_BadPFMuonFilter
       or TheEvent.Flag_BadChargedCandidateFilter
       or TheEvent.Flag_eeBadScFilter
       or TheEvent.Flag_ecalBadCalibFilter):
        isGoodEvent = False

    Trigger24 = (TheEvent.passMu24 and TheEvent.matchMu24_1 
                 and TheEvent.filterMu24_1 and TheEvent.pt_1 > 25.0)
    Trigger27 = (TheEvent.passMu27 and TheEvent.matchMu27_1 
                 and TheEvent.filterMu27_1 and TheEvent.pt_1 > 25.0)
    Trigger2027 = (TheEvent.passMu20Tau27 
                   and TheEvent.matchMu20Tau27_1 
                   and TheEvent.matchMu20Tau27_2
                   and TheEvent.filterMu20Tau27_1                    
                   and TheEvent.filterMu20Tau27_2
                   and TheEvent.pt_1 > 21 and TheEvent.pt_2 > 31 
                   and TheEvent.pt_1 < 25
                   and abs(TheEvent.eta_1) < 2.1
                   and abs(TheEvent.eta_2) < 2.1)
    #no tau trigger matching in embedded
    if(SampleName == "embedded"):
        Trigger2027 = (#TheEvent.passMu20Tau27 
                       #and TheEvent.matchMu20Tau27_1 
                       #asnd TheEvent.filterMu20Tau27_1
                       #and TheEvent.pt_1 > 21 and TheEvent.pt_2 > 31 
            TheEvent.pt_1 > 21 and TheEvent.pt_2 > 31 
            and TheEvent.pt_1 < 25
            and abs(TheEvent.eta_1) < 2.1
            and abs(TheEvent.eta_2) < 2.1)
    if(not Trigger24 and not Trigger27 and not Trigger2027):
        isGoodEvent = False

    if(not TheEvent.againstElectronVLooseMVA6_2 or not TheEvent.againstMuonTight3_2):
        isGoodEvent = False

    #Cecile has some weird stuff here.
    #I don't know what this is or how to port it.
    """
    nbtag=rawnbtag;
    if (sample!="data_obs" && sample!="embedded" && nbtag>0) nbtag=PromoteDemote(h_btag_eff_b, h_btag_eff_c, h_btag_eff_oth, nbtag, bpt_1, bflavor_1, beta_1,0);
    """
    #I should ask what this is...
    #and then figure out how to port it to python.
    if(TheEvent.nbtag>0):
        isGoodEvent = False

    if(TheEvent.pt_2 < 20):
        isGoodEvent = False

    #no overlap with embedded
    if((SampleName == "DY" 
        or SampleName == "TT"    
        or SampleName == "VV") 
       and (TheEvent.gen_match_1 > 2 and TheEvent.gen_match_1 < 6 and TheEvent.gen_match_2 > 2 and TheEvent.gen_match_2 < 6)):
        isGoodEvent = False                
    
    if (TheEvent.q_1*TheEvent.q_2 > 0):
        isGoodEvent = False

    #need a signal region definition.
    signalRegion = (TheEvent.byTightIsolationMVArun2v2DBoldDMwLT_2 and TheEvent.iso_1 < 0.15)
    
    antiIsolated = (TheEvent.byVLooseIsolationMVArun2v2DBoldDMwLT_2 
                    and not TheEvent.byTightIsolationMVArun2v2DBoldDMwLT_2
                    and TheEvent.iso_1 < 0.15)
    
    if(not antiIsolated):
        isGoodEvent = False        

    return isGoodEvent

#We should have no duplicates/
#we just want to cut it down to the selected events
def TrivialPriority(NewEventDictionary,OldEventDictionary):
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jesterworks driven 2017 Anti-Iso Selections")
    parser.add_argument('ConfFiles',nargs="+",help="The files to perform the cuts for")
    
    args = parser.parse_args()
    
    for ConfFile in args.ConfFiles:
        TheSkim = Jesterworks(ConfFile,HTTSelectionCuts,TrivialPriority)
        TheSkim.CreateListOfFilesToRunOn()
        TheSkim.Run()
    """
    ConfFile  =sys.argv[1]
    TheSkim = Jesterworks(ConfFile,HTTSelectionCuts,TrivialPriority)
    TheSkim.CreateListOfFilesToRunOn()
    TheSkim.Run()
    """
