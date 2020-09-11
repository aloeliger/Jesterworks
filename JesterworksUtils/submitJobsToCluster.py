#!/usr/bin/env python 
#Andrew Loeliger
#script/interface for jesterworks to create and submit condor jobs

import os
import argparse
from JesterworksUtils.RecursiveLoader
from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as JesterworksConfiguration
import datetime
import getpass    

def main():
    #okay, we need to sort out what needs to happen here.
    #what is necessary to attempt to run a combine job?
    #a script, with our necessary command
    parser = argparse.ArgumentParser(description='Jesterworks submission tool for running configurations or parts of configurations on condor')
    parser.add_argument('--configFiles','-c',nargs='+',help='configurations to create submissions for',required=True)
    fileNumGroup = parser.add_mutually_exclusive_group(required=True)
    fileNumGroup.add_argument('--all',action='store_true',help='Run all files of the selected configurations')
    fileNumGroup.add_argument('--onlyFile',nargs='+',help='Specify the numbers of files from the configuration to run.',type=int)
    
    #first things first, we should check whether there is a valid proxy.
    #if there isn't let's make one.
    proxyExists = os.system('voms-proxy-info')
    if proxyExists != 0:
        print("Creating proxy...")
        os.system('voms-proxy-init --voms=\"cms\" --valid=192:00')
    
    #now that we have that, let's loop over each of our configurations
    theLoader = JesterworksUtils.RecursiveLoader.RecursiveLoader()
    for configFile in args.configFiles:
        #let's quickly load the module so we have it available in case we need elements of it later. This can be gotten rid of if it is not useful.
        theConfigModule = theLoader.LoadFromDirectoryPath(configFile)
        for item in dir(theConfigModule):
            theConfig = getattr(theConfigModule,item)
            if isinstance(theConfig,JesterworksConfiguration):
                break
        #okay, let's set up a submission directory if that doesn't exist
        overallSubmissionDirectory = '/nfs_scratch/'+getpass.getuser()='/'+(configFile[configFile.rfind('/')+1:len(configFile)-3])
        if not os.path.isdir(ocerallSubmissionDirectory):
            os.mkdir(overallSubmissionDirectory)
            
    

if __name__ == '__main__':
    main()
