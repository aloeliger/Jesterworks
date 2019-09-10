#recoil correction class
import ROOT
import os
import sys

class RecoilCorrection():
    def __init__(self,FileName):
        #class vars
        self._FileName = ""
        self._epsrel = 0.0 
        self._epsabs = 0.0
        self._error = 0.0
        self._range = 0.0
        self._nZPtBins = 0
        self.nJetsBins = 0
        self._metZParalData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._metZPerpData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._metZParalMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._metZPerpMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._metZParalDataHist = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._metZPerpDataHist = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._metZParalMCHist = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._metZPerpMCHist = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._meanMetZParalData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._meanMetZPerpData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._meanMetZParalMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._meanMetZPerpMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._rmsMetZParalData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._rmsLeftMetZParalData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._rmsRightMetZParalData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._rmsMetZParalMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._rmsLeftMetZParalMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._rmsRightMetZParalMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._rmsMetZPerpData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._rmsLeftMetZPerpData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._rmsRightMetZPerpData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        
        self._rmsMetZPerpMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._rmsLeftMetZPerpMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._rmsRightMetZPerpMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._xminMetZPerp = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._xmaxMetZPerp = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._xminMetZPerpData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._xmaxMetZPerpData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._xminMetZPerpMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._xmaxMetZPepMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._xminMetZPerpMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._xmaxMetZPerpMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._xminMetZParalData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._xmaxMetZParalData = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        self._xminMetZParalMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self._xmaxMetZParalMC = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

        #start the init
        cmsswBase = os.environ['CMSSW_BASE']
        baseDir = cmsswBase+"/src"

        self._FileName = baseDir+"/"+FileName
        File = ROOT.TFile(_FileName)
        if(File.IsZombie()):
            print("file "+_FileName+" is not found... quitting ")
            sys.exit()
        projH = File.Get("projH")
        if(projH==None):
            print("File should contain histogram with the name projH")
            print("Check content of the file "+_FileName)

        firstBinStr = projH.GetXaxis().GetBinLabel(1)
        secondBinStr = projH.GetXaxis().GetBinLabel(2)
        
        paralZStr = firstBinStr
        perpZStr = secondBinStr

        if(firstBinStr.find("Perp")>0):
            paralZStr = secondBinStr
            perpZStr = firstBinStr

        print("Parallel component      (U1) : "+str(paralZStr))
        print("Perpendicular component (U2) : "+str(perpZStr))
        ZPtBinsH = File.Get("ZPtBinsH")
        if(ZPtBinsH==None):
            print("File should contain histogram with the name ZPtBinsH ")
            print("Check content of the file "+str(_FileName))
            sys.exit()
        nZPtBins = ZPtBinsH.GetNbinsX()
        ZPtBins=[0,0,0,0,0,0,0,0,0,0]
        ZptStr["","","","","","","","","",""]
        for i in range(nZPtBins):
            ZPtBins[i] = ZPtBinsH.GetXaxis().GetBinLowEdge(i+1)
            if (i<nZPtBins):
                ZPtStr[i] = ZPtBinsH.GetXaxis().GetBinLabel(i+1)
        nJetBinsH = File.Get("nJetBinsH")
        if (nJetBinsH==None):
            print("File should contain histogram with the name nJetBinsH")
            print("Check content of the file "+_FileName)
            sys.exit()
        nJetsBins = nJetBinsH.GetNbinsX()
        nJetsStr=["","","","",""]
        for i in range(nJetsBins):
            nJetsStr[i] = nJetBinsH.GetXaxis().GetBinLabel(i+1)

        self.InitMEtWeights(File,
                            perpZStr,
                            paralZStr,
                            nZPtBins,
                            ZPtBins,
                            ZPtStr,
                            nJetsBins,
                            nJetsStr)
        self._epsrel = 5e-4
        self._epsabs = 5e-4
        self._range = 0.95
    
    def Correct(MetPx,MetPy,genVPx,genVPy,visVPx,vixVPy,njets,MetCorrsPx):
        Zpt = ROOT.TMath.Sqrt(genVPx*genVPx+genVPy*genVPy)
        U1 = 0 
        U2 = 0
        metU1 = 0
        metU2 = 0
        self.CalculateU1U2FromMet(MetPx,
                                  MetPy,
                                  genVPx,
                                  genVPy,
                                  visVPx,
                                  visVPy,
                                  U1,
                                  U2,
                                  metU1,
                                  metU2)
        if (Zpt>1000):
            Zpt = 999
        if (njets >= self._nJetsBins):
            njets = self._nJetsBins - 1
        ZptBin = self.binNumber(Zpt,self._ZPtBins)
        
        self.U1U2CorrectionsByWidth(U1,
                                    U2,
                                    ZptBin,
                                    njets)
        self.CalculateMetFromU1U2(U1,U2,genVPx,genVpy,visVPx,visVPy,MetCorrPx,MetCorrPy)

    def binNumber(x,bins):
        for iB in range(len(bins)):
            if x>=bins[iB] and x < bins[iB+1]:
                return iB
            return 0

    def binNumber(x,nbins,bins):
        binN = 0
        for ib in range(nbins):
            if (x>=bins[iB] and x < bins[iB+1]):
                binN = iB
                break
        return binN    

    def InitMEtWeights(_File,
                       _perpZStr,
                       _paralZStr,
                       nZPtBins,
                       ZPtBins,
                       _ZPtStr,
                       nJetsBins,
                       _nJetsStr):
        newZPtBins=[]
        newZPtStr=[]
        newNJetsStr=[]

        newPerpZStr = _perpZStr
        newParalZStr = _paralZStr

        for idx in range(nZPtBins+1):
            newZPtBins.append(ZPtBins[idx])
        for idx in range(nZPtBins):
            newZPtStr.append(_ZPtStr[idx])
        for idx in range(nJetsBins):
            newNJetsStr.append(_nJetsStr[idx])

        self.InitMEtWeights(_File,
                            newZPtBins,
                            newPerpZStr,
                            newParalZStr,
                            newZPtStr,
                            newNJetsStr)
    def InitMEtWeights(_FileMet,
                       ZPtBins,
                       _perpZStr
                       _paralZStr,
                       _ZPtStr,
                       _nJetsStr):
        self._nZPtBins = len(ZPtBins)-1
        self._nJetsBins = len(_nJetsStr)
        self._ZPtBins = ZPtBins

        for ZPtBin in range(_nZPtBins):
            for jetBin in range(_nJetsBins):
                binStrPerpData = _perpZStr  + "_" + _nJetsStr[jetBin] + _ZPtStr[ZPtBin] + "_data"
                binStrParalData= _paralZStr + "_" + _nJetsStr[jetBin] + _ZPtStr[ZPtBin] + "_data"
                binStrPerpMC   = _perpZStr  + "_" + _nJetsStr[jetBin] + _ZPtStr[ZPtBin] + "_mc"
                binStrParalMC  = _paralZStr + "_" + _nJetsStr[jetBin] + _ZPtStr[ZPtBin] + "_mc"
                
                self._metZParalData[ZPtBin][jetBin] = _fileMet.Get(binStrParalData)
                self._metZPerpData[ZPtBin][jetBin] = _fileMet.Get(binStrPerpData)
                self._metZParalMC[ZPtBin][jetBin] = _fileMet.Get(binStrParalMC)
                self._metZPerpMC[ZPtBin][jetBin] = _fileMet.Get(binStrPerpMC)
                
                if (self._metZParalData[ZPtBin][jetBin] == None):
                    print("Function with name "+binStrParalData+" is not found file "+self._FileName)
                    sys.exit()
                if (self._metZPerpData[ZPtBin][jetBin] == None):
                    print("Function with name "+binStrPerpData+" is not found file "+self._FileName)
                    sys.exit()
                if (self._metZParalMC[ZPtBin][jetBin] == None):
                    print("Function with name "+binStrParalMC+" is not found file "+self._FileName)
                    sys.exit()
                if (self._metZPerpMC[ZPtBin][jetBin] == None):
                    print("Function with name "+binStrPerpMC+" is not found file "+self._FileName)
                    sys.exit()
                
                print(str(_ZPtStr[ZPtBin])+" : "+_nJetsStr[jetBin])
                      
                xminD = 0.0
                xmaxD = 0.0
                
                self._metZParalData[ZPtBin][jetBin].GetRange(xminD,xmaxD)
                self._xminMetZParalData[ZPtBin][jetBin] = float(xminD)
                self._xmaxMetZParalData[ZPtBin][jetBin] = float(xmaxD)
                
                self._metZPerpData[ZPtBin][jetBin].GetRange(xminD,xmaxD)
                self._xminMetZPerpData[ZPtBin][jetBin] = float(xminD)
                self._xminMetZPerpData[ZPtBin][jetBin] = float(xmaxD)

                self._metZParalMC[ZPtBin][jetBin].GetRange(xminD,xmaxD)
                self._xminMetZPerpMC[ZPtBin][jetBin] = float(xminD)
                self._xmaxMetZPerpMC[ZPtBin][jetBin] = float(xmaxD)

                self._xminMetZParalData[ZPtBin][jetBin] = self._metZParalData[ZPtBin][jetBin].Mean(self._xminMetZParalData[ZPtBin][jetBin],self._xmaxMetZParalData[ZPtBin][jetBin])
                self._rmsMetZParalData[ZPtBin][jetBin] = ROOT.TMath.Sqrt(self._metZParalData[ZPtBin][jetBin].CentralMoment(2,self._xminMetZParalData[ZPtBin][jetBin],self._xmaxMetZParalData[ZPtBin][jetBin]))
                self._meanMetZPerpData[ZPtBin][jetBin] = 0
                self._rmsMetZPerpData[ZPtBin][jetBin] = ROOT.TMath.Sqrt(self._metZPerpData[ZPtBin][jetBin].CentralMoment(2,self._xminMetZPerpData[ZPtBin][jetBin],self._xmaxMetZParalData[ZPtBin][jetBin]))

                self._meanMetZParalMC[ZPtBin][jetBin] = self._metZParalMC[ZPtBin][jetBin].Mean(self._xminZParalMC[ZPtBin][jetBin],self._xmaxMetZParalMC[ZPtBin][jetBin])
                self._rmsMEtZParalMC[ZPtBin][jetBin] = ROOT.TMath.Sqrt(self._metZParalMC[ZPtBin][jetBin].CentralMoment(2,self._xminMetZParalMC[ZPtBin][jetBin],self._xmaxMetZParalMC[ZPtBin][jetBin]))
                self._meanMetZPerpMC[ZPtBin][jetBin] = 0
                self._rmsMetZPerpMC[ZPtBin][jetBin] = ROOT.TMath.Sqrt(self._metZPerpMC[ZPtBin][jetBin].CentralMoment(2,_xminMetZPerpMC[ZPtBin][jetBin],self._xmaxMetZPerpMC[ZPtBin][jetBin]))

    def CalculateU1U2FromMet(metPx,metPy,genZPx,genZPy,diLepPx,diLepPy,U1,U2,metU1,metU2):
        hadRecX = metPx+diLepPx-genZPx
        hadRecy - metPy+diLepPy-genZPy

        hadRecpt = ROOT.TMath.Sqrt(hadRecX*hadRecX-hadRecY*hadRecY)

        phihadRec = ROOT.TMath.ATan2(hadRecY,hadRecX)

        phiDiLep = ROOT.TMath.ATan2(diLepPy,diLepPx)
        
        phiMEt = ROOT.TMath.ATan2(metPy,metPx)

        metPt = ROOT.TMath.Sqrt(metPx*metPx+metPy*metPy)

        phiZ = ROOT.TMath.Sqrt(genZPy,genZPx)

        deltaPhiZHadRec = phiHadRec - phiZ
        deltaPhiDiLepMEt = phiMEt - phiDiLep

        U1 = hadRecPt * ROOT.TMath.Cos(deltaPhiZHadRec)
        U2 = hadRecPt * ROOT.TMath.Sin(deltaPhiZHadRec)

        metU1 = metPt * ROOT.TMath.Cos(deltaPhiDiLepMEt)
        metU2 = metPt * ROOT.TMath.Sin(deltaPhiDiLepMEt)

    def CalculateMetFromU1U2(U1,U2,genZPx,genZPy,diLepPx,diLepPy,metPx,metPy):
        hadRecPt = ROOT.TMath.Sqrt(U1*U1+U2*U2)
        deltaPhiZHadRec = ROOT.TMath.ATan2(U2,U1)

        phiZ = ROOT.TMath.ATan2(genZPy,genZPx)

        phiHadRec = PhiZ + deltaPhiZHadRec

        metPx = hadRecX + genZPx - diLepPx
        metPy = hadRecY + genZPy - diLepPy

    def U1U2CorrectionsByWidth(U1,U2,ZptBin,njets):
        if njets>=self._nJetsBins:
            njets = self._nJetsBins-1
        width = U1 - self._meanMetZParalMC[ZPtBin][njets]
        width = width * self._rmsMetZParalData[ZptBin][njets]/self._rmsMetZParalMC[ZptBin][njets]
        u1 = self._meanMetZParalData[ZptBin][njets] + width
        
        width = U2
        width = width * self._rmsMetZPerpData[ZptBin][njets]/self._rmsMetZPerpMC[ZptBin][njets]
        U2 = width

    def rescale(x,meanData,meanMC,resolutionData,resolutionMC):
        width = x - meanMC
        width = width * resoultionData/resolutionMC
        return meanData + width

    def CorrectionsBySampling(x,funcMC,funcData):
        nSumProb = 1
        q = [0.0]
        sumProb = [0.0]
        
        xD = x

        xminD = 0
        xmaxD = 0

        funcMC.GetRange(xminD,xmaxD)

        xmin = xminD

        sumProb[0] = funcMC.INtegralOneDim(xmin,xD,self._epsrel,self._epsabs,self._error)

        funcData.GetQunatiles(nSumProb,q,sumProb)

        output = q[0]

        return output
