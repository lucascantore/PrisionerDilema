from Prisoner import Prisoner

"""
TitForTat: a Prisoner who copies their opponent's last choice.
"""
class TitForTat(Prisoner):
    
    """
    This strategy requires remembering the opponent's
    last choice, so the class overrides the constructor
    to initialize a field to store this information. The
    value initially stored in last_strategy will be the 
    strategy picked for the first round.
    """
    def __init__(self):
        self.last_strategy = True
        self.name = "TitForTat"

    @staticmethod
    def name():
        return "TitForTat"
    
    """
    This Prisoner always does what their opponent did last
    """
    def pick_strategy(self):
        return self.last_strategy
    
    """
    This Prisoner also has to remember their opponent's last strategy
    """
    def process_results(self, my_strategy, other_strategy):
        self.last_strategy = other_strategy
