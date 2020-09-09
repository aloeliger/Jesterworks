#!/user/bin/env python
#Andrew Loeliger
#quick module designed to provide a few utility functions for interfacing with DAS

import subprocess

def getListOfDasFiles(
        primaryDataset='',
        processedDataset='',
        dataTier='NANOAOD'):
    #okay, first thing to do is get a list of the sets that are matched
    #this is done with a call to the dasclient, and loaded via subprocess
    finalList = []
    dasCommand = [
        'dasgoclient',
        '--query=dataset dataset=/'+primaryDataset+'/'+processedDataset+'/'+dataTier+'',
        '--limit=0',
        ]

    #print dasCommand
    dasProcess = subprocess.Popen(
        dasCommand,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    datasetOut, datasetErr = dasProcess.communicate()
    dasExitcode = dasProcess.wait()

    if dasExitcode <> 0:
        raise RuntimeError(
            'das.py crashed with error:\n%s' % \
            datasetErr+datasetOut ) #sometimes das sends the crash message to stdout
    datasets = datasetOut.split('\n')
    datasets.pop()
    #print datasets
    #now for each dataset that matches the initial condition, let's get a list of files in each dataset, and attach it to the final return
    for dataset in datasets:
        dasCommand = [
        'dasgoclient',
        '--query=file dataset='+dataset,
        '--limit=0',
        ]
        
        dasProcess = subprocess.Popen(
            dasCommand,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        fileOut, fileErr = dasProcess.communicate()
        dasExitcode = dasProcess.wait()

        if dasExitcode <> 0:
            raise RuntimeError(
                'das.py crashed with error:\n%s' % \
                fileErr+fileOut ) #sometimes das sends the crash message to stdout
            
        fileList = fileOut.split('\n')
        fileList.pop()
        #print dataset
        #print fileList
        finalList+=fileList
    print finalList
        
        
