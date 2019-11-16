import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.Triggers_18_MC as Triggers
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MT
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.DR as DeltaR
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.TES as TES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MES as MES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.LLFakeES as LLFakeES

MCCollection = BranchDef.UserBranchCollection()
MCCollection.UserBranches = [Triggers.Trigger24,
                             Triggers.Trigger27,
                             Triggers.Trigger2027,
                             MT.MTBranch,
                             DeltaR.DeltaRBranch,
                             TES.TES_E_UP_2018Branch,
                             TES.TES_E_DOWN_2018Branch,
                             TES.TES_PT_UP_2018Branch,
                             TES.TES_PT_DOWN_2018Branch,
                             TES.TES_MET_UP_2018Branch,
                             TES.TES_MET_DOWN_2018Branch,
                             TES.TES_METPhi_UP_2018Branch,
                             TES.TES_METPhi_DOWN_2018Branch,
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
