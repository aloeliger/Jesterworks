#Main jesterworks run script
import ROOT
import JesterworksUtils.RecursiveLoader
import JesterworksUtils.Colors as Colors
import argparse
from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as JesterworksConfiguration

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jesterworks rnning script for skimming and selecting from root trees")
    parser.add_argument("--ConfigFiles",nargs="+",help="Python based configurations files used to specify output",required=True)

    args = parser.parse_args()

    TheLoader = JesterworksUtils.RecursiveLoader.RecursiveLoader()
    for ConfigFile in args.ConfigFiles:
        TheConfigModule = TheLoader.LoadFromDirectoryPath(ConfigFile)
        #scan the contents of the module looking for an
        #instance of a configuration        
        for item in dir(TheConfigModule):
            TheConfig = getattr(TheConfigModule,item)
            if isinstance(TheConfig,JesterworksConfiguration):
                break
        #set up the output file
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
        TheChain = TheChain.CopyTree(TheConfig.CutConfig.CreateFinalCutString())
        #if the configuration has an end action, perform it
        if TheConfig.EndAction != None:
            TheConfig.EndAction.PerformEndAction(TheConfig.EndAction,TheChain,TheConfig,OutputFile)
        #write it out
        TheChain.Write()
        print(Colors.GREEN+"[>>Complete<<]"+Colors.ENDC+" "+ConfigFile)
