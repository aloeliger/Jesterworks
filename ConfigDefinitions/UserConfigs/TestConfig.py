from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config

from ConfigDefinitions.BranchAdditions.UserDefinedCollections.TestCollection import TestCollection as BranchCollection
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.TestCutConfig import TestCutConfig as TestCutConfig
from ConfigDefinitions.EndActionDefinitions.UserConfigs.GrabHistograms import HistogramGrabber as HistogramGrabber

TestConfig = Config()
TestConfig.Path = "/data/ccaillol/smhmt2018_svfitted_4aug/"
TestConfig.Files = ["DY.root"]
TestConfig.InputTreeName = "mutau_tree"
TestConfig.SampleName = "DY"
TestConfig.OutputPath = "/data/aloeliger/"
TestConfig.OutputFile = "Test.root"
TestConfig.OutputTreeName = "mt_Selected"
TestConfig.BranchCollection = BranchCollection
TestConfig.CutConfig = TestCutConfig
TestConfig.EndAction = HistogramGrabber
