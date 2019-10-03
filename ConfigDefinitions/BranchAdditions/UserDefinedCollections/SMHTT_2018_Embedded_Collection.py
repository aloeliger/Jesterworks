import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.Triggers_18_Embedded as Triggers
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MT

EmbeddedCollection = BranchDef.UserBranchCollection()
EmbeddedCollection.UserBranches=[Triggers.Trigger24,
                                 Triggers.Trigger27,
                                 Triggers.Trigger2027,
                                 MT.MTBranch]
