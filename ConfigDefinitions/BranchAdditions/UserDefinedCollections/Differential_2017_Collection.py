import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.TES as TES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MES as MES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.LLFakeES as LLFakeES
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.RivetMjj as RivetMjj
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.Fiducial as Fiducial
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.HiggsMass as HiggsMass
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.HiggsEta as HiggsEta
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.HiggsPhi as HiggsPhi
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.HiggsPt as HiggsPt
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.VisibleMass as VisibleMass
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.VisibleEta as VisibleEta
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.VisiblePhi as VisiblePhi
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.VisiblePt as VisiblePt
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.MTBranch as MTBranch
import ConfigDefinitions.BranchAdditions.UserDefinedBranches.DifferentialHiggsPt as DifferentialHiggsPt

DifferentialCollection = BranchDef.UserBranchCollection()
DifferentialCollection.UserBranches = [
    TES.TES_E_UP_2017Branch,
    TES.TES_E_DOWN_2017Branch,
    TES.TES_PT_UP_2017Branch,
    TES.TES_PT_DOWN_2017Branch,
    TES.TES_MET_UP_2017Branch,
    TES.TES_MET_DOWN_2017Branch,
    TES.TES_METPhi_UP_2017Branch,
    TES.TES_METPhi_DOWN_2017Branch,
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
    RivetMjj.RivetMjjBranch,
    Fiducial.FiducialBranch,
    HiggsEta.HiggsEtaBranch,
    HiggsMass.HiggsMassBranch,
    HiggsPhi.HiggsPhiBranch,
    HiggsPt.HiggsPtBranch,
    VisibleEta.VisibleEtaBranch,
    VisibleMass.VisibleMassBranch,
    VisiblePhi.VisiblePhiBranch,
    VisiblePt.VisiblePtBranch,
    MTBranch.MTBranch,
    DifferentialHiggsPt.differentialHiggsPtBranch,
]
