import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.Triggers_16 as Triggers
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MT

SMHTT_2016_Collection = BranchDef.UserBranchCollection()
SMHTT_2016_Collection.UserBranches =  [Triggers.Trigger22,
                                       Triggers.Trigger1920,
                                       MT.MTBranch]
