"""
Prisoner superclass
"""

import random
class Falco():

    """
    Constructor. Called once at the start of each match.
    If needed, override this method to initialize any 
    auxiliary data you want to use to determine your 
    Prisoner's strategy. This data will persist between
    rounds of a match but not between matches.
    """
    def __init__(self):
        self.name = "Falco"
        self.other_strategy = False
        self.my_strategy = False
        self.other_ultimo_consent = 3

    @staticmethod
    def name():
        return "Falco"
    
    """
    Pick a strategy: return True to cooperate; return False to defect.
    If not overridden, the Prisoner will always cooperate.
    """
    def pick_strategy(self):
        if self.other_ultimo_consent > 2:
            return False
        r = random.randint(1, 100)
        s = random.randint(1, 100)
        if (not self.other_strategy & s <= 75) | (self.my_strategy & r <= 20):
            return False
        else:
            return self.my_strategy | r <= 60

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
        self.my_strategy = my_strategy
        self.other_strategy = other_strategy
        if other_strategy:
            self.other_ultimo_consent = 0
        else:
            self.other_ultimo_consent += 1
