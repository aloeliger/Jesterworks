#!/usr/bin/env python 
#Andrew Loeliger
#script/interface for jesterworks to create and submit condor jobs

import os
import argparse
from Jesterworks.JesterworksUtils.RecursiveLoader import RecursiveLoader
from ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as JesterworksConfiguration
import datetime
import getpass    
import subprocess
import re

#create a submission file for use on condor
#do it at the specified location.
def createSubmissionFile(fileName):
    #let's create the submission file at the specified location
    #this should be an explicit creation of the file
    theFile = open(fileName,'x')
    #we need to make sure we know where our proxy is.
    #this will have information specific to user, so we have no choice really
    #except parsing some information and figuring it out ourself
    vomsProxyInfoCommand = ['voms-proxy-info']
    vomsProxyInfoProcess = subprocess.Popen(
        vomsProxyInfoCommand,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    vomsProxyInfoOut, vomsProxyInfoErr = vomsProxyInfoProcess.communicate()
    vomsProxyInfoExitcode = vomsProxyInfoProcess.wait()

    if vomsProxyInfoExitcode <> 0:
        raise RuntimeError(
            'voms proxy info error: %s' % vomsProxyInfoOut+vomsProxyInfoErr
            )
    #okay, now let's find the location and name of the voms proxy
    proxyFileLocation = re.search('(?:path\s+:\s)(/.*)*',vomsProxyInfoOut).group(1)
    theFile.Write('X509UserProxy        = '+proxyFileLocation+'\n')
    

def main():    
    parser = argparse.ArgumentParser(description='Jesterworks submission tool for running configurations or parts of configurations on condor')
    parser.add_argument('--configFiles','-c',nargs='+',help='configurations to create submissions for',required=True)
    fileNumGroup = parser.add_mutually_exclusive_group(required=True)
    fileNumGroup.add_argument('--all',action='store_true',help='Run all files of the selected configurations')
    fileNumGroup.add_argument('--onlyFiles',nargs='+',help='Specify the numbers of files from the configuration to run.',type=int)
    
    #first things first, we should check whether there is a valid proxy.
    #if there isn't let's make one.
    proxyExists = os.system('voms-proxy-info')
    if proxyExists != 0:
        print("Creating proxy...")
        os.system('voms-proxy-init --voms=\"cms\" --valid=192:00')
    
    #now that we have that, let's loop over each of our configurations
    theLoader = RecursiveLoader()
    for configFile in args.configFiles:
        #let's quickly load the module
        theConfigModule = theLoader.LoadFromDirectoryPath(configFile)
        for item in dir(theConfigModule):
            theConfig = getattr(theConfigModule,item)
            if isinstance(theConfig,JesterworksConfiguration):
                break
        #okay, let's set up a submission directory if that doesn't exist
        configFileDirectoryName = configFile[configFile.rfind('/')+1:len(configFile)-3]+datetime/datetime.now().strftime('%d%m%y_%H%M')
        overallSubmissionDirectory = '/nfs_scratch/'+getpass.getuser()+'/'+configFileDirectoryName
        if not os.path.isdir(overallSubmissionDirectory):
            os.mkdir(overallSubmissionDirectory)
        #okay, at this point, let's consider whether we are doing this for all files of a configuration, or whether
        # we are doing this only for specific files. 
        indicesToProcess = []
        if args.all:
            indicesToProcess = range(0,len(theConfig.Files))
        elif args.onlyFiles != None:
            indicesToProcess = args.onlyFiles
        for fileIndex in indicesToProcess:
            #let's set up a directory specifically for whichever file it is we want to submit
            fileNumSpecificName = overallSubmissionDirectory+'/'+configFileDirectoryName+''
            if not os.path.isdir(overallSubmissionDirectory):
                os.mkdir(fileNumSpecificName)
                
            #okay, our next job is to go ahead and make a submission file for this specific file we want to submit.
            
    

if __name__ == '__main__':
    main()
