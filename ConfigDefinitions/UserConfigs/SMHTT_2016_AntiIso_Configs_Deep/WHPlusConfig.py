from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2016_Collection import SMHTT_2016_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2016Cuts_AntiIso_MC_Data_wDeep import SMHTT2016Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2016_svfitted_12oct/"
DataConfig.Files = ["WplusH125.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "WHPlus"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2016_AntiIso_Deep/"
DataConfig.OutputFile = "WHPlus.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber