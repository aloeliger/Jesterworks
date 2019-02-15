import ROOT
import sys
from Jesterworks import Jesterworks

def TauIDSkim(TheEvent,SampleName=""):
    TauVector = ROOT.TLorentzVector()
    MuVector = ROOT.TLorentzVector()
    TauVector.SetPtEtaPhiM(TheEvent.tPt,TheEvent.tEta,TheEvent.tPhi,TheEvent.tMass)
    MuVector.SetPtEtaPhiM(TheEvent.mPt,TheEvent.mEta,TheEvent.mPhi,TheEvent.mMass)
    if(TheEvent.IsoMu27Pass
       and TheEvent.m_t_DR>0.5
       and MuVector.Pt() > 28 
       and TauVector.Pt() > 19
       and abs(MuVector.Eta()) < 2.4
       and abs(TauVector.Eta()) < 2.3
       and TheEvent.mPFIDMedium 
       and TheEvent.mRelPFIsoDBDefault < 0.15 
       and TheEvent.eVetoZTTp001dxyzR0 == 0
       and TheEvent.muVetoZTTp001dxyzR0 <= 1
       and TheEvent.dimuonVeto == 0
       and TheEvent.tAgainstMuonTight3
       and TheEvent.tAgainstElectronVLooseMVA6):
        return True
    else:
        return False
    return False


def TauIDPriority(NewEventDictionary,OldEventDictionary):
    if(NewEventDictionary["mPt"]>OldEventDictionary["mPt"] 
       or (NewEventDictionary["mPt"]>OldEventDictionary["mPt"]-0.00001
           and NewEventDictionary["tPt"] > OldEventDictionary["tPt"])):
        return True
    else:
        return False

if __name__=="__main__":
    TheSkim = Jesterworks(sys.argv[1],TauIDSkim,TauIDPriority)
    TheSkim.CreateListOfFilesToRunOn()
    TheSkim.Run()
