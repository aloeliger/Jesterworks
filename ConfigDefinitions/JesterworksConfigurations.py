# Defines the jesterworks configuration class
# this will be used as a common template for user based inheritances
import ROOT
import glob
import ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import ConfigDefinitions.CuttingDefinitions.CutDef as CutDef

class JesterworksConfiguration():
    def __init__(self):
        self.Path = ""
        self.Files=[]
        self.InputTreeName = ""
        self.SampleName = ""
        self.OutputPath = ""
        self.OutputFile = ""
        self.OutputTreeName = ""
        self.BranchCollection = BranchDef.UserBranchCollection()
        self.CutConfig = CutDef.UserCutConfig()
    def ReturnCompleteListOfFiles(self):
        return [self.Path+File for File in self.Files]
    def CreateListOfFilesForDirectory(self):
        self.Files += glob.glob(self.Path+"*.root")
