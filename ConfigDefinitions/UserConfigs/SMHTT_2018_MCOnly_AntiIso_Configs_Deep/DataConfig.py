from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2018_Data_Collection import DataCollection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2018Cuts_MC_Data_AntiIso_wDeep import SMHTT2018Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2018_svfitted_30sep/"
DataConfig.Files = ["Data.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "Data"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2018_MCOnly_AntiIso_Deep/"
DataConfig.OutputFile = "Data.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
