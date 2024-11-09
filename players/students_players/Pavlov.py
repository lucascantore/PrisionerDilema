"""
Prisoner superclass
"""
class Pavlov():

    """
    Constructor. Called once at the start of each match.
    If needed, override this method to initialize any 
    auxiliary data you want to use to determine your 
    Prisoner's strategy. This data will persist between
    rounds of a match but not between matches.
    """
    def __init__(self):
        self.cr = self.dr = 0
        self.prev_strategy = None
        self.name = "Pavlov"

    @staticmethod
    def name():
        return "Pavlov"
    
    """
    Pick a strategy: return True to cooperate; return False to defect.
    If not overridden, the Prisoner will always cooperate.
    """
    def pick_strategy(self):
        if self.prev_strategy is None:
            self.prev_strategy = True
            return True
        
        if self.cr > self.dr:
            return True
        
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
        if my_strategy and not other_strategy:
            self.dr += 5
        elif not my_strategy and other_strategy:
            self.cr += 5
        elif my_strategy and other_strategy:
            self.cr += 2
            self.dr += 2
        elif not my_strategy and not other_strategy:
            self.dr += 1
            self.cr += 1
