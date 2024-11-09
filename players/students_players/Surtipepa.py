"""
Prisoner superclass
"""

import random

class Surtipepa:

    """
    Constructor. Called once at the start of each match.
    If needed, override this method to initialize any 
    auxiliary data you want to use to determine your 
    Prisoner's strategy. This data will persist between
    rounds of a match but not between matches.
    """
    def __init__(self):
        self.name = "Surtipepa"
        self.N = self.sum_other_strategy = 0
        self.proba_anterior_confesar = 0
        self.proba_confesion = 0.002

    @staticmethod
    def name():
        return "Surtipepa"
    
    """
    Pick a strategy: return True to cooperate; return False to defect.
    If not overridden, the Prisoner will always cooperate.
    """
    def pick_strategy(self):
        # Si el enemigo tiene mucha tendencia a confesar, nosotros confesamos con probabilidad muy baja
        random_integer=random.randint(0,100)
        if random_integer < self.proba_confesion*100:
            return True
        else:
            return False
    """
    Process the results of a round. This provides an opportunity to
    store data that preserves memory of previous rounds.
    
    Parameters
    ----------
    my_strategy: bool
        This Prisoner's strategy
        
    other_strategy: bool
        The opponent's strategy
    """
    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        proba_actual = self.sum_other_strategy / self.N
        if other_strategy == True:
            self.sum_other_strategy += 1

        if self.N % 10 == 0:
            if self.proba_anterior_confesar < proba_actual:
                self.proba_confesion += 0.005
                self.proba_confesion=min(self.proba_confesion,0.03)
            else:
                self.proba_confesion -= 0.005
                self.proba_confesion = max(0, self.proba_confesion)
            self.proba_anterior_confesar = proba_actual

