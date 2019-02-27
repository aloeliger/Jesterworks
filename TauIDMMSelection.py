import ROOT
import sys
from Jesterworks import Jesterworks

def TauIDSkim(TheEvent,SampleName=""):
    MuVectorOne = ROOT.TLorentzVector()
    MuVectorTwo = ROOT.TLorentzVector()
    MuVectorOne.SetPtEtaPhiM(TheEvent.m1Pt,TheEvent.m1Eta,TheEvent.m1Phi,TheEvent.m1Mass)
    MuVectorTwo.SetPtEtaPhiM(TheEvent.m2Pt,TheEvent.m2Eta,TheEvent.m2Phi,TheEvent.m2Mass)
    if(TheEvent.IsoMu27Pass
       and TheEvent.m1_m2_DR>0.5
       and MuVectorOne.Pt() >= 27 
       and MuVectorTwo.Pt() >= 27
       and abs(MuVectorOne.Eta()) < 2.4
       and abs(MuVectorTwo.Eta()) < 2.4
       and TheEvent.m1PFIDMedium 
       and TheEvent.m1RelPFIsoDBDefault < 0.15 
       and TheEvent.m2PFIDMedium
       and TheEvent.m2RelPFIsoDBDefault < 0.15 
       and TheEvent.eVetoZTTp001dxyzR0 == 0
       and TheEvent.muVetoZTTp001dxyzR0 <= 2):
        return True
    else:
        return False
    return False


def TauIDPriority(NewEventDictionary,OldEventDictionary):
    if(NewEventDictionary["m1Pt"]>OldEventDictionary["m1Pt"] 
       or (NewEventDictionary["m1Pt"]>OldEventDictionary["m1Pt"]-0.00001
           and NewEventDictionary["m2Pt"] > OldEventDictionary["m2Pt"])):
        return True
    else:
        return False

if __name__=="__main__":
    TheSkim = Jesterworks(sys.argv[1],TauIDSkim,TauIDPriority)
    TheSkim.CreateListOfFilesToRunOn()
    TheSkim.Run()
