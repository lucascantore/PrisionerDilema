"""
Prisoner superclass
"""

from Prisoner import Prisoner
import random


class TraidorProbabilistico():

    """
    Constructor. Called once at the start of each match.
    If needed, override this method to initialize any 
    auxiliary data you want to use to determine your 
    Prisoner's strategy. This data will persist between
    rounds of a match but not between matches.
    """
    def __init__(self):
        self.name = "TraidorProbabilistico"
        self.partidasjugadas = 0          # Numero total de rondas jugadas
        self.cooperaciones = 0            # Cantidad de veces que coopere
        self.traiciones = 0               # Cantidad de veces que el oponente me traiciono
        self.proba_coop = 1.0             # Probabilidad inicial de cooperar

    @staticmethod
    def name():
        return "TraidorProbabilistico"
    
    """
    Pick a strategy: return True to cooperate; return False to defect.
    If not overridden, the Prisoner will always cooperate.
    """
    def pick_strategy(self):
                # Disminuyo la probabilidad de cooperar si me traicionan
        if self.partidasjugadas > 0:  # para no dividir x cero
            self.proba_coop = max(0.1, 1.0 - (self.traiciones / self.partidasjugadas))

        # Genero un nro aleatorio para ver si coopero
        if random.random() < self.proba_coop:
            return True  # Coopero
        else:
            return False  # Traiciono

    
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
        self.partidasjugadas += 1  
        
        if other_strategy == False:
            self.traiciones += 1  #Sumo una traicion

        if my_strategy == True:
            self.cooperaciones += 1  #Sumo una cooperacion