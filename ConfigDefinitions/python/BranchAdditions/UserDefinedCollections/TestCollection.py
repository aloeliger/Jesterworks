#create a quick test collection to test adding a branch to stuff

import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MTBranchDef

TestCollection = BranchDef.UserBranchCollection()
TestCollection.UserBranches = [MTBranchDef.MTBranch]
