#an end  action for grabbing the commonly defined FSA histograms for event production
# and pileup so that proper weightings can be applied to the ntuple.
import ROOT
import ConfigDefinitions.EndActionDefinitions.EndActionDef as EndActionDef

def GrabHistograms(TheEndAction,TheChain,TheConfig,OutputFile):
    FirstHistogram = True
    for File in TheConfig.ReturnCompleteListOfFiles():
        if FirstHistogram:
            InputFile = ROOT.TFile(File)
            nevents = InputFile.Get("nevents").Clone()
            pileup_mc = InputFile.Get("pileup_mc").Clone()
            FirstHistogram = False
        else:
            InputFile = ROOT.TFile(File)
            nevents.Add(InputFile.Get("nevents"))
            pileup_mc.Add(InputFile.Get("pileup_mc"))
            InputFile.Close()
    OutputFile.cd()
    nevents.Write()
    pileup_mc.Write()

HistogramGrabber = EndActionDef.UserEndAction()
HistogramGrabber.PerformEndAction = GrabHistograms
