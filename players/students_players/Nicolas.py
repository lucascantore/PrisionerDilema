from Prisoner import Prisoner
import random

class Nicolas(Prisoner):
    def __init__(self):
        self.OD =  self.D =0 # OD = oponente disiente, D = yo disiento
        self.eC = 0
        self.N = 1
        self.name = "Nicolas"

    @staticmethod
    def name():
        return "Nicolas"
    
    def pick_strategy(self): # True = cooperar, False = disentir
        if self.OD/self.N >= 0.7:
            if(random.random() > 0.5):
                return True
            else:
                return False
        elif self.D > 5:
            return True
        else:
            return False
    
    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy == False:
            self.D+=1
        else:
            self.D = 0
        if other_strategy == False:
            self.OD += 1
        
    
