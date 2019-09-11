#an end  action for grabbing the commonly defined FSA histograms for event production
# and pileup so that proper weightings can be applied to the ntuple.
import ROOT
import ConfigDefinitions.EndActionDefinitions.EndActionDef as EndActionDef

def GrabHistograms(TheEndAction,TheChain,TheConfig,OutputFile):
    FirstHistogram = True
    nevents = ROOT.TH1F()
    pileup_mc = ROOT.TH1F()
    for File in TheConfig.ReturnCompleteListOfFiles():
        #print(type(nevents))
        if FirstHistogram:
            FirstInputFile = ROOT.TFile(File)
            nevents = FirstInputFile.Get("nevents").Clone()
            pileup_mc = FirstInputFile.Get("pileup_mc").Clone()
            FirstHistogram = False
        else:
            InputFile = ROOT.TFile(File)
            nevents.Add(InputFile.Get("nevents"))       
            pileup_mc.Add(InputFile.Get("pileup_mc"))
            InputFile.Close()
        #print(type(nevents))
    OutputFile.cd()
    nevents.SetNameTitle("eventCount","eventCount")
    nevents.Write()
    pileup_mc.Write()
    FirstInputFile.Close()

HistogramGrabber = EndActionDef.UserEndAction()
HistogramGrabber.PerformEndAction = GrabHistograms
