from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2017_MC_Data_Collection import MC_Data_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2017Cuts_MC_NoEmbeddedOverlap_wDeep import SMHTT2017Cuts as CutConfig
from ConfigDefinitions.BranchAdditions.UserDefinedCollections.EScaleCollection_2017 import EScaleCollection  as PostfixCollection
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2017_svfitted_12oct/"
DataConfig.Files = ["ST_t_top.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "VV"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2017_Deep/"
DataConfig.OutputFile = "ST_t_top.root"
DataConfig.OutputTreeName = 'mt_Selected'
DataConfig.BranchCollection = BranchCollection
DataConfig.PostfixBranchCollection = PostfixCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
