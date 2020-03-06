from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2016_Embedded_Collection import SMHTT_2016_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2016Cuts_AntiIso_Embedded_wDeep import SMHTT2016Cuts as CutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

EmbeddedConfig = Config()
EmbeddedConfig.Path = '/data/ccaillol/smhmt2016_svfitted_2mar/'
EmbeddedConfig.Files = ["embedded.root"]
EmbeddedConfig.InputTreeName = 'mutau_tree'
EmbeddedConfig.SampleName = "Embedded"
EmbeddedConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2016_AntiIso_Deep/"
EmbeddedConfig.OutputFile = 'Embedded.root'
EmbeddedConfig.OutputTreeName = 'mt_Selected'
EmbeddedConfig.BranchCollection = BranchCollection
EmbeddedConfig.CutConfig = CutConfig
EmbeddedConfig.EndAction = HistogramGrabber
