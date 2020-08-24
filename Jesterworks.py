#Main jesterworks run script
import ROOT
import JesterworksUtils.RecursiveLoader
import JesterworksUtils.Colors as Colors
from JesterworksUtils.CutFlowCreator import CutFlowCreator
import argparse
from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as JesterworksConfiguration
import sys
import os
import traceback

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jesterworks rnning script for skimming and selecting from root trees")
    parser.add_argument("--ConfigFiles",nargs="+",help="Python based configurations files used to specify output",required=True)
    parser.add_argument("--CreateCutFlow",help="Create a cutflow histogram for the file and store it",action="store_true")

    args = parser.parse_args()

    TheLoader = JesterworksUtils.RecursiveLoader.RecursiveLoader()
    NumErrors = 0
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
            #if len(TheConfig.Files)>1:                
            TheChain = ROOT.TChain(TheConfig.InputTreeName)
            for File in TheConfig.ReturnCompleteListOfFiles():
                TheChain.Add(File)
            #print("Compressing to tree")
            OutputFile.cd()
            TheChain = TheChain.CopyTree("")
            #else:                
            #    inputFile = ROOT.TFile.Open(TheConfig.Path+TheConfig.Files[0])
            #    TheChain = inputFile.Get(TheConfig.InputTreeName).Clone()            
            #OutputFile.cd()
            #TheChain.Write()
            #exit()
            if TheConfig.BranchCollection != None:
                #print("Prepping the collection")
                TheConfig.BranchCollection.PrepCollection(TheChain)
                #print("Adding the Branches")
                TheConfig.BranchCollection.AddBranches(TheChain)
            # if we have any branch corrections to do, do them
            if TheConfig.BranchCorrections != None:
                TheChain = TheConfig.BranchCorrections.GetCorrectedTree(TheChain)
            #before we do the final cutting, let's create the cutflow histogram
            if args.CreateCutFlow:
                cutFlowHandler = CutFlowCreator()
                cutFlowHandler.CreateCutFlow(TheConfig,TheChain)
            #this line handles all the cutting.            
            #print("Doing cutting")
            OutputFile.cd()
            TheChain = TheChain.CopyTree(TheConfig.CutConfig.CreateFinalCutString())
            #if we have any post-fix branches to add, let's do that now
            #print("Doing post branches")
            try:
                TheConfig.PostfixBranchCollection != None
                TheConfig.PostfixBranchCollection.PrepCollection(TheChain)
                TheConfig.PostfixBranchCollection.AddBranches(TheChain)
            except AttributeError:
                #print "Postfix creation error!"
                #traceback.print_exc()
                pass
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
            #if we made a cutflow, write that as well
            if args.CreateCutFlow:
                cutFlowHandler.cutFlowHistogram.Write()
        except Exception as error:
            sys.stdout.write(Colors.RED+"[>>  Error!  <<]"+Colors.ENDC+" "+ConfigFile+"\n")
            sys.stdout.flush()            
            traceback.print_exc()
            NumErrors+=1

        else:
            sys.stdout.write(Colors.GREEN+"[>> Complete <<]"+Colors.ENDC+" "+ConfigFile+"\n")
            sys.stdout.flush()
    if(NumErrors > 0):
        print("There were "+str(NumErrors)+" error(s).")
        print("Please check them and resubmit.")
    else:
        print("Completed with no errors!")
