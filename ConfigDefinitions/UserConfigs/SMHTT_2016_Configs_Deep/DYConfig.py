from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2016_Collection import SMHTT_2016_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2016Cuts_wDeep import SMHTT2016Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Files = ["/data/ccaillol/smhmt2016_svfitted_16aug/DY.root",
                    "/data/ccaillol/smhmt2016_svfitted_16aug/DY1.root",
                    "/data/ccaillol/smhmt2016_svfitted_16aug/DY2.root",
                    "/data/aloeliger/SMHTT/smhmt2016_svfitted_25aug/DY3.root",
                    "/data/aloeliger/SMHTT/smhmt2016_svfitted_25aug/DY4.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "DY"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2016_Deep/"
DataConfig.OutputFile = "DY.root"
DataConfig.OutputTreeName = "mt_Selected"
DataConfig.BranchCollection = BranchCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
