#Test cut configuration
import ConfigDefinitions.CuttingDefinitions.CutDef as CutDef

TestCutConfig = CutDef.UserCutConfig()
TestCutConfig.Cuts.append("pt_2 > 30")
TestCutConfig.Cuts.append("MT < 50")
