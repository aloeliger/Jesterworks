from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2018_MC_Collection import MCCollection as BranchCollection
from ConfigDefinitions.BranchAdditions.UserDefinedCollections.Differential_2018_Collection import DifferentialCollection as PostfixCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2018Cuts_MC_wDeep import SMHTT2018Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2018_svfitted_13jul/"
DataConfig.Files = ["GGZHLLTT.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "ZH125"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2018_Deep/"
DataConfig.OutputFile = "GGZHLLTT.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.PostfixBranchCollection = PostfixCollection
DataConfig.EndAction = HistogramGrabber
