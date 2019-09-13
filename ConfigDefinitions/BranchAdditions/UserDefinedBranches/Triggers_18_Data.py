import ConfigDefinitions.BranchAdditions.BranchDef as Branch

def CalculateTrigger24(TheBranch,TheChain):
    if (TheChain.passMu24 and TheChain.matchMu24_1 
        and TheChain.filterMu24_1 and TheChain.pt_1 > 25.0):
        TheBranch.BranchValue[0]=1.0
    else:
        TheBranch.BranchValue[0]=0.0
def CalculateTrigger27(TheBranch,TheChain):
    if(TheChain.passMu27 and TheChain.matchMu27_1 
       and TheChain.filterMu27_1 and TheChain.pt_1 > 25.0):
        TheBranch.BranchValue[0]=1.0
    else:
        TheBranch.BranchValue[0]=0.0
        
def CalculateTrigger2027(TheBranch,TheChain):
    if TheChain.run >= 317509:
        if (TheChain.passMu20HPSTau27 
            and TheChain.matchMu20HPSTau27_1
            and TheChain.matchMu20HPSTau27_2
            and TheChain.pt_1 > 21 and TheChain.pt_1 < 25
            and TheChain.pt_2 > 28
            and abs(TheChain.eta_1) < 2.1
            and abs(TheChain.eta_2) < 2.1
            and TheChain.filterMu20HPSTau27_1
            and TheChain.filterMu20HPSTau27_2):
            TheBranch.BranchValue[0] = 1.0
        else:
            TheBranch.BranchValue[0] = 0.0
    if TheChain.run < 317509:
        if (TheChain.passMu20Tau27 
            and TheChain.matchMu20Tau27_1
            and TheChain.matchMu20Tau27_2
            and TheChain.pt_1 > 21 and TheChain.pt_1 < 25
            and TheChain.pt_2 > 28
            and abs(TheChain.eta_1) < 2.1
            and abs(TheChain.eta_2) < 2.1
            and TheChain.filterMu20Tau27_1
            and TheChain.filterMu20Tau27_2):
            TheBranch.BranchValue[0] = 1.0
        else:
            TheBranch.BranchValue[0] = 0.0

Trigger24 = Branch.UserBranch()
Trigger24.Name = "Trigger24"
Trigger24.CalculateValue = CalculateTrigger24

Trigger27 = Branch.UserBranch()
Trigger27.Name = "Trigger27"
Trigger27.CalculateValue = CalculateTrigger27

Trigger2027 = Branch.UserBranch()
Trigger2027.Name = "Trigger2027"
Trigger2027.CalculateValue = CalculateTrigger2027
