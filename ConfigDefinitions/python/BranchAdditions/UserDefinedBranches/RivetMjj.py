import ConfigDefinitions.BranchAdditions.BranchDef as Branch
import ROOT

def CalculateRivetMjj(theBranch,theChain):
    Rivet_mjj = -1.0
    jetOneVector = ROOT.TLorentzVector()
    jetTwoVector = ROOT.TLorentzVector()
    if theChain.Rivet_nJets30 > 1:
        jetOneVector.SetPtEtaPhiM(theChain.Rivet_j1pt,theChain.Rivet_j1eta,theChain.Rivet_j1phi,theChain.Rivet_j1m)
        jetTwoVector.SetPtEtaPhiM(theChain.Rivet_j2pt,theChain.Rivet_j2eta,theChain.Rivet_j2phi,theChain.Rivet_j2m)
        Rivet_mjj = (jetOneVector+jetTwoVector).M()
    theBranch.BranchValue[0] = Rivet_mjj

RivetMjjBranch = Branch.UserBranch()
RivetMjjBranch.Name = "Rivet_mjj"
RivetMjjBranch.CalculateValue = CalculateRivetMjj 
