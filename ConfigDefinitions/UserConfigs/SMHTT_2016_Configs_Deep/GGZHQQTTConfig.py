from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2016_Collection import SMHTT_2016_Collection as BranchCollection
from ConfigDefinitions.BranchAdditions.UserDefinedCollections.Differential_2016_Collection import DifferentialCollection as PostfixCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2016Cuts_MC_wDeep import SMHTT2016Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2016_svfitted_13jul/"
DataConfig.Files = ["GGZHQQTT.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "ZH"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2016_Deep/"
DataConfig.OutputFile = "GGZHQQTT.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.PostfixBranchCollection = PostfixCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
