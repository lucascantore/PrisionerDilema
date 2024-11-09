from Prisoner import Prisoner

"""
Prisoner superclass
"""
class AndyDufresne(Prisoner):

    """
    Constructor. Called once at the start of each match.
    If needed, override this method to initialize any 
    auxiliary data you want to use to determine your 
    Prisoner's strategy. This data will persist between
    rounds of a match but not between matches.
    """
    def __init__(self):
        self.oC_ultimas_seg = 2 # Cantidad de veces seguidas que el oponente cooperó.
                                # 2 porque queremos empezar cooperando.
        self.name="Andy Dufresne"

    @staticmethod
    def name():
        return "Andy Dufresne"
    
    """
    Pick a strategy: return True to cooperate; return False to defect.
    If not overridden, the Prisoner will always cooperate.
    """
    def pick_strategy(self):
        if(self.oC_ultimas_seg >= 2): # Cooperamos en la primera ronda o si el otro cooperó al menos dos veces seguidas.
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
        if(other_strategy):
            self.oC_ultimas_seg += 1
        else:
            self.oC_ultimas_seg = 0
