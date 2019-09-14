# a set of globals for calculating uiseful vectors for MT channel skimming
import ConfigDefinitions.GlobalsDefinitions.GlobalsDef as GlobalsDef
import ROOT

def CalculateMTSkimmingGlobals(TheGlobals,TheChain):
    TheGlobals.MuVector.SetPtEtaPhiM(TheChain.mPt,TheChain.mEta,TheChain.mPhi,TheChain.mMass)
    TheGlobals.TauVector.SetPtEtaPhiM(TheChain.tPt,TheChain.tEta,TheChain.tPhi,TheChain.tMass)
    TheGlobals.MetVector.SetPtEtaPhiM(TheChain.type1_pfMetEt,0,TheChain.type1_pfMetPhi,0)
    TheGlobals.Met_UESUp_Vector.SetPtEtaPhiM(TheChain.type1_pfMet_shiftedPt_UnclusteredEnUp,
                                             0,
                                             TheChain.type1_pfMet_shiftedPhi_UnclusteredEnUp,
                                             0)
    TheGlobals.Met_UESDown_Vector.SetPtEtaPhiM(TheChain.type1_pfMet_shiftedPt_UnclusteredEnDown,
                                               0,
                                               TheChain.type1_pfMet_shiftedPhi_UnclusteredEnDown,
                                               0)
    if(TheChain.tZTTGenMatching==5 and TheChain.tDecayMode==0):
        TheGlobals.MetVector = TheGlobals.MetVector+TheGlobals.TauVector-1.007*TheGlobals.TauVector
        TheGlobals.Met_UESUp_Vector = TheGlobals.Met_UESUp_Vector+TheGlobals.TauVector-1.007*TheGlobals.TauVector
        TheGlobals.Met_UESDown_Vector = TheGlobals.Met_UESDown_Vector+TheGlobals.TauVector-1.007*TheGlobals.TauVector
    elif(TheChain.tZTTGenMatching==5 and TheChain.tDecayMode==1):
        TheGlobals.MetVector = TheGlobals.MetVector+TheGlobals.TauVector-0.998*TheGlobals.TauVector
        TheGlobals.Met_UESUp_Vector = TheGlobals.Met_UESUp_Vector+TheGlobals.TauVector-0.998*TheGlobals.TauVector
        TheGlobals.Met_UESDown_Vector = TheGlobals.Met_UESDown_Vector+TheGlobals.TauVector-0.998*TheGlobals.TauVector
    elif(TheChain.tZTTGenMatching==5 and TheChain.tDecayMode==10):
        TheGlobals.MetVector = TheGlobals.MetVector+TheGlobals.TauVector-1.001*TheGlobals.TauVector
        TheGlobals.Met_UESUp_Vector = TheGlobals.Met_UESUp_Vector+TheGlobals.TauVector-1.001*TheGlobals.TauVector
        TheGlobals.Met_UESDown_Vector = TheGlobals.Met_UESDown_Vector+TheGlobals.TauVector-1.001*TheGlobals.TauVector
    if((TheChain.tZTTGenMatching==1 or TheChain.tZTTGenMatching==3)  and TheChain.tDecayMode==0):
        TheGlobals.MetVector = TheGlobals.MetVector+TheGlobals.TauVector-1.003*TheGlobals.TauVector
        TheGlobals.Met_UESUp_Vector = TheGlobals.Met_UESUp_Vector+TheGlobals.TauVector-1.003*TheGlobals.TauVector
        TheGlobals.Met_UESDown_Vector = TheGlobals.Met_UESDown_Vector+TheGlobals.TauVector-1.003*TheGlobals.TauVector
    elif((TheChain.tZTTGenMatching==1 or TheChain.tZTTGenMatching==3)  and TheChain.tDecayMode==1):
        TheGlobals.MetVector = TheGlobals.MetVector+TheGlobals.TauVector-1.036*TheGlobals.TauVector
        TheGlobals.Met_UESUp_Vector = TheGlobals.Met_UESUp_Vector+TheGlobals.TauVector-1.036*TheGlobals.TauVector
        TheGlobals.Met_UESDown_Vector = TheGlobals.Met_UESDown_Vector+TheGlobals.TauVector-1.036*TheGlobals.TauVector

    #recoil correction stuff
    

MTSkimmingGlobals = GlobalsDef.UserGlobals()
MTSkimmingGlobals.TauVector() = ROOT.TLorentzVector()
MTSkimmingGlobals.MuVector() = ROOT.TLorentzVector()
MTSkimmingGlobals.MetVector() = ROOT.TLorentzVector()
MTSkimmingGlobals.Met_UESUp_Vector() = ROOT.TLorentzVector()
MTSkimmingGlobals.Met_UESDown_Vector() = ROOT.TLorentzVector()

MTSkimmingGlobals.CalculateGlobals = CalculateMTSkimmingGlobals
