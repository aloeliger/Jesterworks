#a quick class used for loading other modules in the package in a convenient way

class RecursiveLoader():
    def __init__(self):
        pass
    def LoadPath(self,PathToLoad):
        Module = __import__(PathToLoad)
        ToLoad = PathToLoad.split('.')
        if len(ToLoad) == 1:
            return Module
        else:            
            for i in range(1,len(ToLoad)):
                Module = getattr(Module,ToLoad[i])                
            return Module
    def LoadFromDirectoryPath(self,PathToLoad):
        #trim the .py file extension off
        PathToLoad=PathToLoad[:len(PathToLoad)-3]
        PathToLoad=PathToLoad.replace("/",".")        
        return self.LoadPath(PathToLoad)
        
    def LoadFromCMSSWPath(self,pathToLoad):
        #okay, let's get rid of any explicit mentions of "python" in the path to load
        print pathToLoad
        if 'python/' in pathToLoad:
            pathToLoad = pathToLoad.replace('python/','')
        #let's also add on the overall module name so we can load this from a CMSSW
        if not 'Jesterworks/' in pathToLoad:
            pathToLoad = 'Jesterworks/'+pathToLoad            
        print pathToLoad
        return self.LoadFromDirectoryPath(pathToLoad)
