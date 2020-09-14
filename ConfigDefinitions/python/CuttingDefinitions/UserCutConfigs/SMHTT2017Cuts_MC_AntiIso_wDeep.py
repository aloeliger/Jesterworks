import ConfigDefinitions.CuttingDefinitions.CutDef as CutDef

SMHTT2017Cuts = CutDef.UserCutConfig()
SMHTT2017Cuts.Cuts=[]
SMHTT2017Cuts.Cuts.append("abs(eta_1) < 2.1 && abs(eta_2) < 2.3")
SMHTT2017Cuts.Cuts.append("!(Flag_goodVertices || Flag_globalSuperTightHalo2016Filter || Flag_HBHENoiseFilter || Flag_HBHENoiseIsoFilter || Flag_EcalDeadCellTriggerPrimitiveFilter || Flag_BadPFMuonFilter || Flag_ecalBadCalibReducedMINIAODFilter)")
SMHTT2017Cuts.Cuts.append("Trigger24 || Trigger27 || Trigger2027")
SMHTT2017Cuts.Cuts.append("byVLooseDeepVSe_2 && byTightDeepVSmu_2")
SMHTT2017Cuts.Cuts.append("DeltaR > 0.5")
#SMHTT2017Cuts.Cuts.append("nbtag <= 0 && nbtagL <= 1")
SMHTT2017Cuts.Cuts.append("pt_2 > 20")
#SMHTT2017Cuts.Cuts.append("!(gen_match_1 > 2 && gen_match_1 < 6 && gen_match_2 > 2 && gen_match_2 < 6)")
#SMHTT2017Cuts.Cuts.append("gen_match_2 != 6")
SMHTT2017Cuts.Cuts.append("q_1 * q_2 < 0")
SMHTT2017Cuts.Cuts.append("byVVVLooseDeepVSjet_2 && !byMediumDeepVSjet_2 && iso_1 < 0.15")
