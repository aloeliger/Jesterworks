from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.SMHTT_2017_MC_Data_Collection import MC_Data_Collection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.SMHTT2017Cuts_TTContamination import SMHTT2017Cuts as CutConfig
from ConfigDefinitions.BranchAdditions.UserDefinedCollections.Differential_2017_Collection import DifferentialCollection as PostfixCollection
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

DataConfig = Config()
DataConfig.Path = "/data/ccaillol/differentialmt2017_svfitted_3aug/"
DataConfig.Files = ["TTTo2L2Nu.root"]
DataConfig.InputTreeName = "mutau_tree"
DataConfig.SampleName = "TT"
DataConfig.OutputPath = "/data/aloeliger/SMHTT_Selected_2017_TTContamination/"
DataConfig.OutputFile = "TTTo2L2Nu.root"
DataConfig.OutputTreeName = 'mt_Selected'
DataConfig.BranchCollection = BranchCollection
DataConfig.PostfixBranchCollection = PostfixCollection
DataConfig.CutConfig = CutConfig
DataConfig.EndAction = HistogramGrabber
