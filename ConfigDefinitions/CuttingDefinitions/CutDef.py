#Quick class for creating and merging our cut strings

class UserCutConfig():
    def __init__(self):
        self.CutString=""
        self.Cuts=[]
    def CreateFinalCutString(self):
        for Cut in self.Cuts:
            self.CutString+="("+Cut+")&&"
        self.CutString = self.CutString[:len(self.CutString)-2]
        return self.CutString
