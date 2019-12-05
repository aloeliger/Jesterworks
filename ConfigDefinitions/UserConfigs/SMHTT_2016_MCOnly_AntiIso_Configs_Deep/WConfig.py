from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2016_Collection import SMHTT_2016_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2016Cuts_AntiIso_MC_wDeep import SMHTT2016Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/smhmt2016_svfitted_20nov/"
DataConfig.Files = ["W.root",
                    "W1.root",
                    "W2.root",
                    "W3.root",
                    "W4.root",]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "W"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2016_MCOnly_AntiIso_Deep/"
DataConfig.OutputFile = "W.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
