from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2017_MC_Data_Collection import MC_Data_Collection as BranchCollection
from ConfigDefinitions.BranchAdditions.UserDefinedCollections.Differential_2017_Collection import DifferentialCollection as PostfixCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2017Cuts_MC_wDeep import SMHTT2017Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2017_svfitted_13jul/"
DataConfig.Files = ["ggH125.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "ggH"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2017_Deep/"
DataConfig.OutputFile = "ggH.root"
DataConfig.OutputTreeName = 'mt_Selected'
DataConfig.BranchCollection = BranchCollection
DataConfig.PostfixBranchCollection = PostfixCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
