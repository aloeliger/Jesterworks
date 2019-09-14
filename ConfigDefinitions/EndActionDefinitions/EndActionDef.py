#a quick class that just has an action that needs to be overwritten.

class UserEndAction():
    def __init__(self):
        self.PerformEndAction = self.DefaultAction
    def DefaultAction(self,TheChain,TheConfig,OutputFile):
        print("Improperly defined end action!")
        raise RuntimeError()
