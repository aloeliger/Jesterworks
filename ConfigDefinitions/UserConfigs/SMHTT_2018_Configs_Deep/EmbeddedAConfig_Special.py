from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2018_Embedded_Collection import EmbeddedCollection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2018Cuts_Embedded_wDeep import SMHTT2018Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2018_svfitted_12oct/"
DataConfig.Files = ["EmbeddedA.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "EmbeddedA"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2018_Deep/"
DataConfig.OutputFile = "EmbeddedA.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
