import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.HiggsMass as HiggsMass
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.HiggsEta as HiggsEta
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.HiggsPhi as HiggsPhi
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.HiggsPt as HiggsPt
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.VisibleMass as VisibleMass
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.VisibleEta as VisibleEta
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.VisiblePhi as VisiblePhi
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.VisiblePt as VisiblePt
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MTBranch

HiggsVariablesCollection = BranchDef.UserBranchCollection()
HiggsVariablesCollection.UserBranches = [
    HiggsEta.HiggsEtaBranch,
    HiggsMass.HiggsMassBranch,
    HiggsPhi.HiggsPhiBranch,
    HiggsPt.HiggsPtBranch,
    VisibleEta.VisibleEtaBranch,
    VisibleMass.VisibleMassBranch,
    VisiblePhi.VisiblePhiBranch,
    VisiblePt.VisiblePtBranch,
]
