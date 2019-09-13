import ConfigDefinitions.CuttingDefinitions.CutDef as CutDef

SMHTT2018Cuts = CutDef.UserCutConfig()
SMHTT2018Cuts.Cuts=[]
SMHTT2018Cuts.Cuts.append("abs(eta_1)<2.1 && abs(eta_2) < 2.3")
SMHTT2018Cuts.Cuts.append("!(Flag_goodVertices || Flag_globalSuperTightHalo2016Filter || Flag_HBHENoiseFilter || Flag_HBHENoiseIsoFilter || Flag_EcalDeadCellTriggerPrimitiveFilter || Flag_BadPFMuonFilter || Flag_eeBadScFilter || Flag_ecalBadCalibFilter)")
SMHTT2018Cuts.Cuts.append("Trigger24 || Trigger27 || Trigger2027")
SMHTT2018Cuts.Cuts.append("gen_match_2 != 6") #don't overlap with fake factors
SMHTT2018Cuts.Cuts.append("againstElectronVLooseMVA62018_2 && againstMuonTight3_2")
SMHTT2018Cuts.Cuts.append("nbtag <= 0 && nbtagL <= 1")
SMHTT2018Cuts.Cuts.append("pt_2 > 20")
SMHTT2018Cuts.Cuts.append("q_1 * q_2 < 0")
SMHTT2018Cuts.Cuts.append("byVLooseIsolationMVArun2v2DBoldDMwLT_2 && !byTightIsolationMVArun2v2DBoldDMwLT_2 && iso_1 < 0.15")
