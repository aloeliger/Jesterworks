from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2016_Collection import SMHTT_2016_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2016Cuts_MC_wDeep import SMHTT2016Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2016_svfitted_12oct/"
DataConfig.Files = ["ST_tW_antitop.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "ST_tW_antitop"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2016_MCOnly_Deep/"
DataConfig.OutputFile = "ST_tW_antitop.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber