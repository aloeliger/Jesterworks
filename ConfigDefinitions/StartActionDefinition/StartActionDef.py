# a quick class that just has an action that needs to be overwritten

class UserStartAction():
    def __init__(self):
        pass
    def DefaultAction(self,TheChain,TheConfig,OutputFile):
        print("Improperly defined start action!")
        raise RuntimeError()
