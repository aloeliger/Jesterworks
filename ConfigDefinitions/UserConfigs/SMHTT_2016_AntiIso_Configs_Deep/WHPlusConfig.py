from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2016_Collection import SMHTT_2016_Collection as BranchCollection
from ConfigDefinitions.BranchAdditions.UserDefinedCollections.Differential_2016_Collection import DifferentialCollection as PostfixCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2016Cuts_AntiIso_MC_wDeep import SMHTT2016Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/differentialmt2016_svfitted_3aug/"
DataConfig.Files = ["WplusH125.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "WHPlus"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2016_AntiIso_Deep/"
DataConfig.OutputFile = "WHPlus.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.PostfixBranchCollection = PostfixCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
