#a set of classes defining global values (vectors and other things) that can be computed for 
#every single loaded event in a chain. 
#The class is incredibly barebones, and only requires that a defined function is assigned.

import ROOT

class UserGlobals():
    def __init__(self):
        self.CalculateGlobals = self.DefaultCalculateGlobals
    def DefaultCalculateGlobals(self,TheChain):
        raise RuntimeError("Global structure did not have a defined way to calculate useful values!")
