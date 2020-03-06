from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2017_MC_Data_Collection import MC_Data_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2017Cuts_MC_AntiIso_wDeep import SMHTT2017Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/differential_mt2017_svfitted/"
DataConfig.Files = ["VBFHWW.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "VBFHWW"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2017_AntiIso_Deep/"
DataConfig.OutputFile = "VBFHWW.root"
DataConfig.OutputTreeName = 'mt_Selected'
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber