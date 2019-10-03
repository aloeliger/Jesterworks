from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2018_MC_Collection import MCCollection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2018Cuts_MC_Data_AntiIso import SMHTT2018Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2018_svfitted_30sep/"
DataConfig.Files = ["WplusH125.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "WHPlus"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2018_MCOnly_AntiIso/"
DataConfig.OutputFile = "WHPlus.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
