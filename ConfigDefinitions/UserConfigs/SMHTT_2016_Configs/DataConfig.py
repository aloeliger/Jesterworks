from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2016_Collection import SMHTT_2016_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2016Cuts import SMHTT2016Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2016_svfitted_16aug/"
DataConfig.Files = ["Data.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "Data"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2016/"
DataConfig.OutputFile = "Data.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber