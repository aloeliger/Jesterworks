import ROOT

class CutFlowCreator():
    def __init__(self):
        pass
    def CreateCutFlow(self,theConfig,theTree):
        self.CreateCutFlowHistogram(theConfig)
        treeCopy = theTree.CloneTree(-1,"fast")
        #okay, now we run over the cuts that are in the cut config.
        #for each cut in there, cut the tree with it, and then figure out how many 
        #events we have remaining and fill the cut flow histogram to the proper level        
        self.cutFlowHistogram.SetBinContent(1,treeCopy.GetEntries())
        for i in range(len(theConfig.CutConfig.Cuts)):
            treeCopy = treeCopy.CopyTree(theConfig.CutConfig.Cuts[i])
            self.cutFlowHistogram.SetBinContent(i+2,treeCopy.GetEntries())

    def CreateCutFlowHistogram(self,theConfig):
        nCuts = len(theConfig.CutConfig.Cuts)        
        self.cutFlowHistogram = ROOT.TH1F("CutFlow","CutFlow",nCuts+1,0.0,float(nCuts)+1.0)
