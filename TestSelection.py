import ROOT
from Jesterworks import Jesterworks

def TestSkim(TheEvent,SampleName=""):
    TauVector = ROOT.TLorentzVector()
    MuVector = ROOT.TLorentzVector()
    TauVector.SetPtEtaPhiM(TheEvent.tPt,TheEvent.tEta,TheEvent.tPhi,TheEvent.tMass)
    MuVector.SetPtEtaPhiM(TheEvent.mPt,TheEvent.mEta,TheEvent.mPhi,TheEvent.mMass)
    if(TheEvent.IsoMu27Pass
       #and TheEvent.m_t_DR>0.5
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

def TestPriority(NewEventDictionary,OldEventDictionary):
    if(NewEventDictionary["mPt"]>OldEventDictionary["mPt"] 
       or (NewEventDictionary["mPt"]>OldEventDictionary["mPt"]-0.00001
           and NewEventDictionary["tPt"] > OldEventDictionary["tPt"])):
        return True
    else:
        return False
    

if __name__ == "__main__":
    TheSkim = Jesterworks("TestConfig.conf",TestSkim,TestPriority)
    TheSkim.CreateListOfFilesToRunOn()
    TheSkim.PerformSkim()

"""
float pu=1.0;
        tree->GetEntry(iEntry);
        bool print=false;
        if (iEntry % 1000 == 0) fprintf(stdout, "\r  Processed events: %8d ", iEntry);
        fflush(stdout);
        plotFill("pileup_mc",tree->nTruePU,80,0,80);
        if (!tree->IsoMu27Pass) continue;
        TLorentzVector dau1;
        TLorentzVector dau2;
        dau1.SetPtEtaPhiM(tree->mPt,tree->mEta,tree->mPhi,tree->mMass);
        dau2.SetPtEtaPhiM(tree->tPt,tree->tEta,tree->tPhi,tree->tMass);
        if (tree->m_t_DR<0.5) continue;
        if (dau1.Pt()<28 or dau2.Pt()<19) continue;
        if (fabs(dau1.Eta())>2.4 or fabs(dau2.Eta())>2.3) continue;
        if (fabs(tree->tCharge)>1) continue;
        if (!tree->mPFIDMedium or tree->mRelPFIsoDBDefault>0.15) continue;
        evt_now=tree->evt;
        if (tree->eVetoZTTp001dxyzR0>0) continue;
        if (tree->muVetoZTTp001dxyzR0>1) continue;
        if (tree->dimuonVeto>0) continue;
        if (!tree->tAgainstMuonTight3) continue;//FIXME
        if (!tree->tAgainstElectronVLooseMVA6) continue;//FIXME
         if (evt_now!=evt_before){
           mupt_before=tree->mPt;
           muiso_before=tree->mRelPFIsoDBDefault;
           taupt_before=tree->tPt;
           tauiso_before=tree->tByIsolationMVArun2v1DBoldDMwLTraw;
        }
        if (evt_now!=evt_before){
           if (bestEntry>-1)
              fillTree(Run_Tree,tree,bestEntry,isMC,recoil);
           bestEntry=iEntry;
        }
        if (evt_now==evt_before){
           if (tree->mPt>mupt_before or (tree->mPt>mupt_before-0.00001 && tree->tPt>taupt_before)){
                bestEntry=iEntry;
                muiso_before=tree->mRelPFIsoDBDefault;
                mupt_before=tree->mPt;
                tauiso_before=tree->tByIsolationMVArun2v1DBoldDMwLTraw;
                taupt_before=tree->tPt;
           }
        }
        evt_before=evt_now;


"""
