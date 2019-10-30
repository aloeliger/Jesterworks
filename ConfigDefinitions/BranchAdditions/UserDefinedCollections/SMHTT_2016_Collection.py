import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.Triggers_16 as Triggers
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MT
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.VisibleMass as VisibleMass
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.DR as DeltaR

SMHTT_2016_Collection = BranchDef.UserBranchCollection()
SMHTT_2016_Collection.UserBranches =  [Triggers.Trigger22,
                                       Triggers.Trigger1920,
                                       MT.MTBranch,
                                       VisibleMass.VisibleMassBranch,
                                       DeltaR.DeltaRBranch]
