from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2017_MC_Data_Collection import MC_Data_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2017Cuts_MC_wDeep import SMHTT2017Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/differential_mt2017_svfitted/"
DataConfig.Files = ["WminusHWW.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "WminusHWW"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2017_MCOnly_Deep/"
DataConfig.OutputFile = "WminusHWW.root"
DataConfig.OutputTreeName = 'mt_Selected'
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber