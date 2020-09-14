import ConfigDefinitions.BranchAdditions.BranchDef as Branch

def CalculateTrigger22(TheBranch,TheChain):
    if (TheChain.pt_1 >23.0         
        and (
            (TheChain.passMu22eta2p1 
             and TheChain.matchMu22eta2p1_1 
             and TheChain.filterMu22eta2p1_1
             and abs(TheChain.eta_1)<2.1 
         ) 
            or (TheChain.passTkMu22eta2p1 
                and TheChain.matchTkMu22eta2p1_1 
                and TheChain.filterTkMu22eta2p1_1
                and abs(TheChain.eta_1)<2.1 
            )
            or (TheChain.passMu22
                and TheChain.matchMu22_1
                and TheChain.filterMu22_1                
            ) 
            or (TheChain.passTkMu22
                and TheChain.matchTkMu22_1
                and TheChain.filterTkMu22_1
            )
        )):
        TheBranch.BranchValue[0] = 1.0
    else:
        TheBranch.BranchValue[0] = 0.0

def CalculateTrigger1920(TheBranch,TheChain):
    if (TheChain.pt_1 > 20.0 
        and TheChain.pt_1 < 23.0
        and TheChain.pt_2 > 25.0 
        and abs(TheChain.eta_1) < 2.1
        and abs(TheChain.eta_2) < 2.1        
        and (
            (
                TheChain.passMu19Tau20 
                and TheChain.matchMu19Tau20_1 
                and TheChain.matchMu19Tau20_2
                and TheChain.filterMu19Tau20_1
                and TheChain.filterMu19Tau20_2
            ) 
            or 
            (
                TheChain.passMu19Tau20SingleL1 
                and TheChain.matchMu19Tau20SingleL1_1  
                and TheChain.matchMu19Tau20SingleL1_2
                and TheChain.filterMu19Tau20SingleL1_1
                and TheChain.filterMu19Tau20SingleL1_2
            )
        )
         
        
         # no muon filter
        and TheChain.matchEmbFilter_Mu19Tau20_2
    ):
        TheBranch.BranchValue[0] = 1.0
    else:
        TheBranch.BranchValue[0] = 0.0
    
Trigger22 = Branch.UserBranch()
Trigger22.Name = "Trigger22"
Trigger22.CalculateValue = CalculateTrigger22

Trigger1920 = Branch.UserBranch()
Trigger1920.Name = "Trigger1920"
Trigger1920.CalculateValue = CalculateTrigger1920
