from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2018_MC_Collection import MCCollection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2018Cuts_MC_NoEmbeddedOverlap_AntiIso_wDeep import SMHTT2018Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2018_svfitted_30sep/"
DataConfig.Files = ["DY.root","DY1.root","DY2.root","DY3.root","DY4.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "DY"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2018_AntiIso_Deep/"
DataConfig.OutputFile = "DY.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
