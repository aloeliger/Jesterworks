import ROOT
import sys
from Jesterworks import Jesterworks

#return true if good event.
def KITSkim(TheEvent,SampleName=""):
    MuVector = ROOT.TLorentzVector()
    TauVector = ROOT.TLorentzVector()
    MuVector.SetPtEtaPhiM(TheEvent.mPt,TheEvent.mEta,TheEvent.mPhi,TheEvent.mMass)
    TauVector.SetPtEtaPhiM(TheEvent.tPt,TheEvent.tEta,TheEvent.tPhi,TheEvent.tMass)
    if(MuVector.DeltaR(TauVector) >= 0.5
       and abs(TheEvent.mPVDXY) <= 0.045
       and abs(TheEvent.mPVDZ) <= 0.2
       and abs(TheEvent.tPVDZ) <= 0.2
       and MuVector.Pt() >= 21.0 
       and TauVector.Pt() >= 23.0
       and abs(MuVector.Eta()) <= 2.1
       and abs(TauVector.Eta()) <= 2.3
       and TheEvent.tRerunMVArun2v2DBoldDMwLTVVLoose
       and TheEvent.tDecayModeFinding
       and TheEvent.mPFIDMedium
       ):
        return True
        
    else:
        return False
    return False

#return true if we keep the new event
def DefaultPriority(NewEventDictionary,OldEventDictionary):
    if(NewEventDictionary['mRelPFIsoDBDefault'] < OldEventDictionary['mRelPFIsoDBDefault']):
        return True
    elif (NewEventDictionary['mRelPFIsoDBDefault'] == OldEventDictionary['mRelPFIsoDBDefault'] 
          and NewEventDictionary['mPt'] > OldEventDictionary['mPt']):
        return True
    elif (NewEventDictionary['mRelPFIsoDBDefault'] == OldEventDictionary['mRelPFIsoDBDefault'] 
          and NewEventDictionary['mPt'] == OldEventDictionary['mPt'] 
          and NewEventDictionary['tRerunMVArun2v2DBoldDMwLTraw'] > OldEventDictionary['tRerunMVArun2v2DBoldDMwLTraw']):
        return True
    elif(NewEventDictionary['mRelPFIsoDBDefault'] == OldEventDictionary['mRelPFIsoDBDefault'] 
         and NewEventDictionary['mPt'] == OldEventDictionary['mPt'] 
         and NewEventDictionary['tRerunMVArun2v2DBoldDMwLTraw'] == OldEventDictionary['tRerunMVArun2v2DBoldDMwLTraw']
         and NewEventDictionary['tPt'] > OldEventDictionary['tPt']):
        return True
    else
        return False
    return False

if __name__ == "__main__":
    ConfFile = sys.argv[1]
    TheSkim = JesterWorks(ConfFile,KITSkim,DefaultPriority)
    TheSkim.CreateListOfFilesToRunOn()
    TheSkim.PerformSkim()

#Cecile's perfectly synchronized code
"""
 TLorentzVector dau1;
        TLorentzVector dau2;
        dau1.SetPtEtaPhiM(tree->mPt,tree->mEta,tree->mPhi,tree->mMass);
        dau2.SetPtEtaPhiM(tree->tPt,tree->tEta,tree->tPhi,tree->tMass);
        if (isMC && tree->tZTTGenMatching==5 && tree->tDecayMode==0) dau2=dau2*1.007;
        else if (isMC && tree->tZTTGenMatching==5 && tree->tDecayMode==1) dau2=dau2*0.998;
        else if (isMC && tree->tZTTGenMatching==5 && tree->tDecayMode==10) dau2=dau2*1.001;
        if (isMC && (tree->tZTTGenMatching==1 or tree->tZTTGenMatching==3) && tree->tDecayMode==0) dau2=dau2*1.003;
        else if (isMC && (tree->tZTTGenMatching==1 or tree->tZTTGenMatching==3) && tree->tDecayMode==1) dau2=dau2*1.036;
        if (print) cout<<tree->evt<<" "<<tree->tPt<<" "<<dau2.Pt()<<" "<<tree->tZTTGenMatching<<endl;
        if (dau1.DeltaR(dau2)<0.5) continue;
        if (print) cout<<tree->evt<<" dxy,dz"<<endl;
        if (fabs(tree->mPVDXY)>0.045) continue;
        if (fabs(tree->mPVDZ)>0.2) continue;
        if (fabs(tree->tPVDZ)>0.2) continue;
        if (print) cout<<tree->evt<<" pt"<<endl;
        if (dau1.Pt()<21 or dau2.Pt()<23) continue;
        if (print) cout<<tree->evt<<" eta"<<endl;
        if (fabs(dau1.Eta())>2.1 or fabs(dau2.Eta())>2.3) continue;
        if (print) cout<<tree->evt<<" tau iso"<<endl;
        if (!tree->tRerunMVArun2v2DBoldDMwLTVVLoose) continue;
        if (print) cout<<tree->evt<<" tau dm"<<endl;
        if (!tree->tDecayModeFinding) continue;
        if (print) cout<<tree->evt<<" mu id"<<endl;
        if (!tree->mPFIDMedium) continue;
        evt_now=tree->evt;
         if (evt_now!=evt_before){
           mupt_before=tree->mPt;
           muiso_before=tree->mRelPFIsoDBDefault;
           taupt_before=tree->tPt;
           tauiso_before=tree->tRerunMVArun2v2DBoldDMwLTraw;
        }
        if (evt_now!=evt_before){
           if (bestEntry>-1){
              fillTree(Run_Tree,tree,bestEntry,recoil,isMC);
           }
           bestEntry=iEntry;
        }
        if (evt_now==evt_before){
           if (tree->mRelPFIsoDBDefault<muiso_before or (tree->mRelPFIsoDBDefault==muiso_before && tree->mPt>mupt_before) or (tree->mRelPFIsoDBDefault==muiso_before && tree->mPt==mupt_before && tree->tRerunMVArun2v2DBoldDMwLTraw>tauiso_before) or (tree->mRelPFIsoDBDefault==muiso_before && tree->mPt==mupt_before && tree->tRerunMVArun2v2DBoldDMwLTraw==tauiso_before && tree->tPt>taupt_before) ){
                bestEntry=iEntry;
                muiso_before=tree->mRelPFIsoDBDefault;
                mupt_before=tree->mPt;
                tauiso_before=tree->tRerunMVArun2v2DBoldDMwLTraw;
                taupt_before=tree->tPt;
           }
        }

"""
