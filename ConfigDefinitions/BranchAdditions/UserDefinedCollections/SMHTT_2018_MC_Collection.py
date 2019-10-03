import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.Triggers_18_MC as Triggers
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MT

MCCollection = BranchDef.UserBranchCollection()
MCCollection.UserBranches = [Triggers.Trigger24,
                             Triggers.Trigger27,
                             Triggers.Trigger2027,
                             MT.MTBranch]
