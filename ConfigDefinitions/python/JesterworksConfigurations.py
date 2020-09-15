# Defines the jesterworks configuration class
# this will be used as a common template for user based inheritances
import ROOT
import glob
import Jesterworks.ConfigDefinitions.BranchAdditions.BranchDef as BranchDef
import Jesterworks.ConfigDefinitions.CuttingDefinitions.CutDef as CutDef
#import Jesterworks.ConfigDefinitions.GlobalsDefinition.GlobalsDef as GlobalsDef
import Jesterworks.ConfigDefinitions.EndActionDefinitions.EndActionDef as EndActionDef
import Jesterworks.ConfigDefinitions.RenameDefinitions.RenameDef as RenameDef
import Jesterworks.ConfigDefinitions.BranchCorrections.BranchCorrection as BranchCorrection

class JesterworksConfiguration():
    def __init__(self):
        self.Path = ""
        self.Files=[]
        self.InputTreeName = ""
        self.SampleName = ""
        self.OutputPath = ""
        self.OutputFile = ""
        self.OutputTreeName = ""
        self.BranchCollection = None#BranchDef.UserBranchCollection()
        self.CutConfig = CutDef.UserCutConfig()
        self.Globals = None
        self.EndAction = None
        self.RenameScheme = None
        self.BranchCorrections = None
    def ReturnCompleteListOfFiles(self):
        return [self.Path+File for File in self.Files]
    def CreateListOfFilesForDirectory(self):
        self.Files += glob.glob(self.Path+"*.root")
