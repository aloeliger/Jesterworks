#Main jesterworks run script
import ROOT
import JesterworksUtils.RecursiveLoader
import JesterworksUtils.Colors as Colors
import argparse
from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as JesterworksConfiguration
import sys
import os
import traceback

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jesterworks rnning script for skimming and selecting from root trees")
    parser.add_argument("--ConfigFiles",nargs="+",help="Python based configurations files used to specify output",required=True)

    args = parser.parse_args()

    TheLoader = JesterworksUtils.RecursiveLoader.RecursiveLoader()
    for ConfigFile in args.ConfigFiles: 
        try:
            TheConfigModule = TheLoader.LoadFromDirectoryPath(ConfigFile)
            sys.stdout.write(Colors.BLUE+"[>>Processing<<]"+Colors.ENDC+" "+ConfigFile+"\r")
            sys.stdout.flush()
            #scan the contents of the module looking for an
            #instance of a configuration        
            for item in dir(TheConfigModule):
                TheConfig = getattr(TheConfigModule,item)
                if isinstance(TheConfig,JesterworksConfiguration):
                    break
            #set up the output file
            #if the path doesn't exist, create it for the file.
            if not os.path.isdir(TheConfig.OutputPath):
                os.makedirs(TheConfig.OutputPath)
                #create the file
            OutputFile = ROOT.TFile(TheConfig.OutputPath+TheConfig.OutputFile,"RECREATE")
            #get a chain and compress it into a tree
            TheChain = ROOT.TChain(TheConfig.InputTreeName)
            for File in TheConfig.ReturnCompleteListOfFiles():
                TheChain.Add(File)
            TheChain = TheChain.CopyTree("")
            #add on any extra branches we need
            if TheConfig.BranchCollection != None:
                TheConfig.BranchCollection.PrepCollection(TheChain)
                TheConfig.BranchCollection.AddBranches(TheChain)
            #this line handles all the cutting.
            #print(TheChain.GetEntries())
            TheChain = TheChain.CopyTree(TheConfig.CutConfig.CreateFinalCutString())
            #print(TheConfig.CutConfig.CutString)
            #print(TheChain.GetEntries())
            #if the configuration has an end action, perform it
            if TheConfig.EndAction != None:
                TheConfig.EndAction.PerformEndAction(TheConfig.EndAction,TheChain,TheConfig,OutputFile)
                #if the tree has a new output name, switch over to that
            if TheConfig.OutputTreeName != '':
                TheChain.SetNameTitle(TheConfig.OutputTreeName,TheConfig.OutputTreeName)
                #write it out
            #Perform any renaming.
            if TheConfig.RenameScheme != None:
                TheConfig.RenameScheme.PerformTheRenaming(TheChain)
            TheChain.Write()
        except Exception as error:
            sys.stdout.write(Colors.RED+"[>>  Error!  <<]"+Colors.ENDC+" "+ConfigFile+"\n")
            sys.stdout.flush()            
            traceback.print_exc()

        else:
            sys.stdout.write(Colors.GREEN+"[>> Complete <<]"+Colors.ENDC+" "+ConfigFile+"\n")
            sys.stdout.flush()
