from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2017_MC_Data_Collection import MC_Data_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2017Cuts_MC_Data_AntiIso import SMHTT2017Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2017_svfitted_13jun/"
DataConfig.Files = ["DY.root","DY1.root","DY2.root","DY3.root","DY4.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "DY"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2017_MCOnly_AntiIso/"
DataConfig.OutputFile = "DY.root"
DataConfig.OutputTreeName = 'mt_Selected'
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
