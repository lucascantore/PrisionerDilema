"""
Prisoner superclass

"""
from Prisoner import Prisoner
import random

class TitForSomeTats(Prisoner):

    """
    Constructor. Called once at the start of each match.
    If needed, override this method to initialize any 
    auxiliary data you want to use to determine your 
    Prisoner's strategy. This data will persist between
    rounds of a match but not between matches.
    """
    def __init__(self):
        self.last_opp_decision = True # empezamos con True
        self.name = "TitForSomeTats"

    @staticmethod
    def name():
        return "TitForSomeTats"

    
    """
    Pick a strategy: return True to cooperate; return False to defect.
    If not overridden, the Prisoner will always cooperate.
    """
    def pick_strategy(self):
        if not self.last_opp_decision:
            if random.randint(1, 10) <= 9: # 90% de las veces tomo venganza por el defect de mi opp
                return False
        return True # el 10% perdono y coopero
    
        
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
        self.last_opp_decision = other_strategy