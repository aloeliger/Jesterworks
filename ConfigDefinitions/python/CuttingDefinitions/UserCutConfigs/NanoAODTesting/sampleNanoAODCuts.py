#sample cuts to run a NANOAOD file under

from ConfigDefinitions.CuttingDefinitions.CutDef import UserCutConfig as CutConfig

sampleCuts = CutConfig()
sampleCuts.Cuts = []
sampleCuts.Cuts.append('nTau==1')
sampleCuts.Cuts.append('nMuon==1')
sampleCuts.Cuts.append('nJet==2')
