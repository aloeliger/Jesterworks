import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.Triggers_17_MC_Data as Triggers
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MT
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.DR as DeltaR
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.TES as TES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MES as MES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.LLFakeES as LLFakeES

MC_Data_Collection = BranchDef.UserBranchCollection()
MC_Data_Collection.UserBranches = [Triggers.Trigger24,
                                   Triggers.Trigger27,
                                   Triggers.Trigger2027,
                                   MT.MTBranch,
                                   DeltaR.DeltaRBranch,
]
