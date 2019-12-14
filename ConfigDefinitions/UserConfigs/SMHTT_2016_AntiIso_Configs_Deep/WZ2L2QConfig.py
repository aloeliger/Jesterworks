from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2016_Collection import SMHTT_2016_Collection as BranchCollection
from ConfigDefinitions.BranchAdditions.UserDefinedCollections.EScaleCollection_2016 import EScaleCollection as PostfixCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2016Cuts_MC_NoEmbeddedOverlap_wDeep import SMHTT2016Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2016_svfitted_20nov/"
DataConfig.Files = ["WZ2L2Q.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "WZ2L2Q"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2016_AntiIso_Deep/"
DataConfig.OutputFile = "WZ2L2Q.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.PostfixBranchCollection = PostfixCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
