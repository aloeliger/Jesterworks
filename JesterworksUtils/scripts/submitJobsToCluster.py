#!/usr/bin/env python 
#Andrew Loeliger
#script/interface for jesterworks to create and submit condor jobs

import os
import argparse
from Jesterworks.JesterworksUtils.RecursiveLoader import RecursiveLoader
from Jesterworks.ConfigDefinitions.JesterworksConfigurations import JesterworksConfiguration as JesterworksConfiguration
import datetime
import getpass    
import subprocess
import re

#create a submission file for use on condor
#do it at the specified location.

def getSimpleCommandOutput(command):
    theProcess = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        )
    output,error = theProcess.communicate()
    theExitCode = theProcess.wait()
    
    if theExitCode != 0:
        raise RuntimeError('Non zero exit code of basic command: '+command+'\n'+output+'\n'+error)
    return output,error

def createSubmissionFile(initialDir,fileName,configFileName,fileIndex):
    #let's create the submission file at the specified location
    #this should be an explicit creation of the file
    theFile = open(initialDir+'/'+fileName,'w')
    #we need to make sure we know where our proxy is.
    #this will have information specific to user, so we have no choice really
    
    
    #okay, now let's find the location and name of the voms proxy
    vomsProxyInfoOut,vomsProxyInfoErr = getSimpleCommandOutput(['voms-proxy-info'])
    proxyFileLocation = re.search('(?:path\s+:\s)(/.*)*',vomsProxyInfoOut).group(1)
    theFile.write('X509UserProxy        = '+proxyFileLocation+'\n')

    #write out the initial dir for the submission
    theFile.write('InitialDir           = '+initialDir+'\n')
    
    #copy user environment to get most of what we need to make this goofiness run
    theFile.write('getenv = True\n')
    
    #find the location of the jesterworks executable script
    jesterworksLocationOut,jesterworksLocationErr = getSimpleCommandOutput(['which','JesterworksRun.py'])    
    theFile.write('Executable           = '+jesterworksLocationOut)#assumes natively (i.e. no python call) runnable jesterworks script
    
    #jesterworks arguments
    theFile.write('Arguments            = "--ConfigFile '+configFileName+' --runSpecificFiles '+str(fileIndex)+'"\n')

    #let's just do some output logging filing stuff
    outputFileName = fileName[:fileName.find('.')]+'.out'
    theFile.write('output               = '+outputFileName+'\n')

    errFileName = fileName[:fileName.find('.')]+'.err'
    theFile.write('error                = '+errFileName+'\n')

    logFileName = fileName[:fileName.find('.')]+'.log'
    theFile.write('Log                  = '+logFileName+'\n')
    
    #let's just handle some standard memory, disk and cpu request stuff
    #we can add special options for any of these later if we decide we want to change these.
    theFile.write('request_memory       = 3000'+'\n')
    theFile.write('request_disk         = 2048000'+'\n')
    theFile.write('request_cpus         = 1'+'\n')
    theFile.write('WhenToTransferOutput = On_Exit'+'\n')

    #this is the final submission command necessary
    theFile.write('queue'+'\n')
    theFile.close()
def main():    
    parser = argparse.ArgumentParser(description='Jesterworks submission tool for running configurations or parts of configurations on condor')
    parser.add_argument('--configFiles','-c',nargs='+',help='configurations to create submissions for',required=True)
    fileNumGroup = parser.add_mutually_exclusive_group(required=True)
    fileNumGroup.add_argument('--all',action='store_true',help='Run all files of the selected configurations')
    fileNumGroup.add_argument('--onlyFiles',nargs='+',help='Specify the numbers of files from the configuration to run.',type=int)
    
    args = parser.parse_args()
    
    #first things first, we should check whether there is a valid proxy.
    #if there isn't let's make one.
    proxyExists = os.system('voms-proxy-info')
    if proxyExists != 0:
        print("Creating proxy...")
        os.system('voms-proxy-init --voms=\"cms\" --valid=192:00')
    else:
        #occasionally it will find the proxy, but it will be expired,
        #so we need to check for that and create a new one if expired
        proxyOutput, proxyErr = getSimpleCommandOutput('voms-proxy-info')
        proxyTimeLeft = re.search('(?:timeleft\s+:\s)([0-9:]*)',proxyOutput).group(1)
        #print proxyTimeLeft
        if proxyTimeLeft == '0:00:00':
            os.system('voms-proxy-init --voms=\"cms\" --valid=192:00')
    
    #now that we have that, let's loop over each of our configurations
    theLoader = RecursiveLoader()
    for configFile in args.configFiles:
        #let's quickly load the module
        theConfigModule = theLoader.LoadFromCMSSWPath(configFile)
        for item in dir(theConfigModule):
            theConfig = getattr(theConfigModule,item)
            if isinstance(theConfig,JesterworksConfiguration):
                break
        #okay, let's set up a submission directory if that doesn't exist
        configFileDirectoryName = configFile[configFile.rfind('/')+1:len(configFile)-3]+datetime.datetime.now().strftime('%d%m%y_%H%M')
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
            fileNumSpecificName = overallSubmissionDirectory+'/'+configFileDirectoryName+'_'+str(fileIndex)
            if not os.path.isdir(fileNumSpecificName):
                os.mkdir(fileNumSpecificName,)
                
            #okay, our next job is to go ahead and make a submission file for this specific file we want to submit.
            
            submissionFileName = configFileDirectoryName+'.sub'
            createSubmissionFile(fileNumSpecificName,submissionFileName,configFile,fileIndex)
            #okay. now we have a submission file, we can go through and submit all of the configurations
            os.system('condor_submit '+fileNumSpecificName+'/'+submissionFileName)
            
if __name__ == '__main__':
    main()
