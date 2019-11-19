import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.Triggers_18_Data as Triggers
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MT
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.DR as DeltaR
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.TES as TES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MES as MES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.LLFakeES as LLFakeES

DataCollection = BranchDef.UserBranchCollection()
DataCollection.UserBranches=[Triggers.Trigger24,
                             Triggers.Trigger27,
                             Triggers.Trigger2027,
                             MT.MTBranch,
                             DeltaR.DeltaRBranch,                             
]
