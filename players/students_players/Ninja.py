from Prisoner import Prisoner

import random

class Ninja(Prisoner): 

    def __init__(self):
        self.total = 0
        self.cooperado = 0
        self.ultimas10 = 10*[False]
        self.name = "Ninja"

    @staticmethod
    def name():
        return "Ninja"

    def process_results(self, my_strategy, other_strategy):
        
        if (my_strategy == other_strategy == True):
            self.cooperado += 1
    
        self.ultimas10[(self.total) % 10] = other_strategy

        self.total += 1
        


    def pick_strategy(self):

        r = random.randint(0,15)

        if((self.cooperado+2) / (self.total+2) < 0.1):
                return r<1
            
        elif((self.cooperado+2) / (self.total+2) < 0.35):
            if(self.ultimas10.count(True) < 2):
                return r<2
            else:
                return r<11
        
        else:
            if(self.ultimas10.count(True) > 7):
                return False
            else:
                return r<13
