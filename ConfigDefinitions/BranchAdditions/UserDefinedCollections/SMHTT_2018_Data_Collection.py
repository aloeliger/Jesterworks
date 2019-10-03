import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.Triggers_18_Data as Triggers
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MT

DataCollection = BranchDef.UserBranchCollection()
DataCollection.UserBranches=[Triggers.Trigger24,
                             Triggers.Trigger27,
                             Triggers.Trigger2027,
                             MT.MTBranch]
