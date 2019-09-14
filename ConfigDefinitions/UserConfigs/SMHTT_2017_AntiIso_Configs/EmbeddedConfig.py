from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2017_Embedded_Collection import MC_Data_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2017Cuts_Embedded_AntiIso import SMHTT2017Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2017_svfitted_13jun/"
DataConfig.Files = ["embedded.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "embedded"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_AntiIso_Experimental/"
DataConfig.OutputFile = "Embedded.root"
DataConfig.OutputTreeName = 'mt_Selected'
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
