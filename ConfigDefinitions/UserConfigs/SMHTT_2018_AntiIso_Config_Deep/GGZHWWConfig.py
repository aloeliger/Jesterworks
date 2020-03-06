from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2018_MC_Collection import MCCollection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2018Cuts_MC_AntiIso_wDeep import SMHTT2018Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/differential_mt2018_svfitted/"
DataConfig.Files = ["GGZHWW.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "GGZHWW"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2018_AntiIso_Deep/"
DataConfig.OutputFile = "GGZHWW.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
