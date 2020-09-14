#just a basic configuration to see if the nanoAOD files will take basic editing from jesterworks without extensive modifications

from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as Config
from ConfigDefinitions.CuttingDefinitions.UserCutConfigs.NanoAODTesting.sampleNanoAODCuts import sampleCuts as cutConfig

DataConfig = Config()
DataConfig.Path = 'root://cmsxrootd.fnal.gov//'
DataConfig.Files=['/store/data/Run2017B/MET/NANOAOD/UL2017_02Dec2019-v1/70000/5C7B796B-8115-DA42-93AD-A84B66B7657B.root']
DataConfig.InputTreeName = 'Events'
DataConfig.SampleName='Data'
DataConfig.OutputPath='./'
DataConfig.OutputFile = 'Test.root'
DataConfig.OutputTreeName = 'Selected'
DataConfig.CutConfig = cutConfig
