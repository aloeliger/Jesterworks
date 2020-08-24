from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2018_Embedded_Collection import EmbeddedCollection as BranchCollection
from ConfigDefinitions.BranchAdditions.UserDefinedCollections.Differential_2018_Embedded_Collection import DifferentialCollection as PostfixCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2018Cuts_Embedded_wDeep import SMHTT2018Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/differentialmt2018_svfitted_3aug/"
DataConfig.Files = ["Embedded.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "Embedded"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2018_Deep/"
DataConfig.OutputFile = "Embedded.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.PostfixBranchCollection = PostfixCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
