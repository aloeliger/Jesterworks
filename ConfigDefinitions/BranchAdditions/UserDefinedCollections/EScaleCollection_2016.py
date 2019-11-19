import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.TES as TES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MES as MES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.LLFakeES as LLFakeES

EScaleCollection = BranchDef.UserBranchCollection()
EScaleCollection.UserBranches = [
    TES.TES_E_UP_2016Branch,
    TES.TES_E_DOWN_2016Branch,
    TES.TES_PT_UP_2016Branch,
    TES.TES_PT_DOWN_2016Branch,
    TES.TES_MET_UP_2016Branch,
    TES.TES_MET_DOWN_2016Branch,
    TES.TES_METPhi_UP_2016Branch,
    TES.TES_METPhi_DOWN_2016Branch,
    MES.muonES_E_UP_Branch,
    MES.muonES_E_DOWN_Branch,
    MES.muonES_Pt_UP_Branch,
    MES.muonES_Pt_DOWN_Branch,
    MES.muonES_MET_UP_Branch,
    MES.muonES_MET_DOWN_Branch,
    MES.muonES_METPhi_UP_Branch,
    MES.muonES_METPhi_DOWN_Branch,
    LLFakeES.EES_E_UP_Branch,
    LLFakeES.EES_E_DOWN_Branch,
    LLFakeES.EES_Pt_UP_Branch,
    LLFakeES.EES_Pt_DOWN_Branch,
    LLFakeES.EES_MET_UP_Branch,
    LLFakeES.EES_MET_DOWN_Branch,
    LLFakeES.EES_METPhi_UP_Branch,
    LLFakeES.EES_METPhi_DOWN_Branch,
    LLFakeES.MES_E_UP_Branch,
    LLFakeES.MES_E_DOWN_Branch,
    LLFakeES.MES_Pt_UP_Branch,
    LLFakeES.MES_Pt_DOWN_Branch,
    LLFakeES.MES_MET_UP_Branch,
    LLFakeES.MES_MET_DOWN_Branch,
    LLFakeES.MES_METPhi_UP_Branch,
    LLFakeES.MES_METPhi_DOWN_Branch,
]
