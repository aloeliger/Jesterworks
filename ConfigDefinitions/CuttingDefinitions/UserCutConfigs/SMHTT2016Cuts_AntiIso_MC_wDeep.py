#Create the 2016 cuts for everything
from ConfigDefinitions.CuttingDefinitions.CutDef import UserCutConfig as CutConfig

SMHTT2016Cuts = CutConfig()
SMHTT2016Cuts.Cuts = []
SMHTT2016Cuts.Cuts.append("abs(eta_1)<2.1 && abs(eta_2)<2.3")
SMHTT2016Cuts.Cuts.append("!(Flag_goodVertices || Flag_globalSuperTightHalo2016Filter || Flag_HBHENoiseIsoFilter || Flag_HBHENoiseFilter || Flag_EcalDeadCellTriggerPrimitiveFilter || Flag_BadPFMuonFilter)")
SMHTT2016Cuts.Cuts.append("Trigger22 || Trigger1920")
SMHTT2016Cuts.Cuts.append("byVVVLooseDeepVSe_2 && byTightDeepVSmu_2")
SMHTT2016Cuts.Cuts.append("nbtag <= 0 && nbtagL <= 1")
SMHTT2016Cuts.Cuts.append("pt_1 > 20.0 && pt_2 > 20.0")
SMHTT2016Cuts.Cuts.append("gen_match_2 != 6")#avoid overlap with FF's
SMHTT2016Cuts.Cuts.append("DeltaR > 0.5")
SMHTT2016Cuts.Cuts.append("q_1 * q_2 < 0")
SMHTT2016Cuts.Cuts.append("byVVVLooseDeepVSjet_2 && !byMediumDeepVSjet_2 && iso_1 < 0.15")
