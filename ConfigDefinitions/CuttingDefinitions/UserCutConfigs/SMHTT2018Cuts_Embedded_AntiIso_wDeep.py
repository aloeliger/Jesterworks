import ConfigDefinitions.CuttingDefinitions.CutDef as CutDef

SMHTT2018Cuts = CutDef.UserCutConfig()
SMHTT2018Cuts.Cuts=[]
SMHTT2018Cuts.Cuts.append("abs(eta_1)<2.1 && abs(eta_2) < 2.3")
SMHTT2018Cuts.Cuts.append("!(Flag_goodVertices || Flag_globalSuperTightHalo2016Filter || Flag_HBHENoiseFilter || Flag_HBHENoiseIsoFilter || Flag_EcalDeadCellTriggerPrimitiveFilter || Flag_BadPFMuonFilter || Flag_eeBadScFilter || Flag_ecalBadCalibReducedMINIAODFilter)")
SMHTT2018Cuts.Cuts.append("Trigger24 || Trigger27 || Trigger2027")
#SMHTT2018Cuts.Cuts.append("gen_match_2 != 6")#avoid overlap with FF's
SMHTT2018Cuts.Cuts.append("byVLooseDeepVSe_2 && byTightDeepVSmu_2")
SMHTT2018Cuts.Cuts.append("DeltaR > 0.5")
#SMHTT2018Cuts.Cuts.append("nbtag <= 0 && nbtagL <= 1")
SMHTT2018Cuts.Cuts.append("nbtag <= 0")
SMHTT2018Cuts.Cuts.append("pt_2 > 20")
SMHTT2018Cuts.Cuts.append("q_1 * q_2 < 0")
SMHTT2018Cuts.Cuts.append("byVVVLooseDeepVSjet_2 && !byMediumDeepVSjet_2 && iso_1 < 0.15")
