from Prisoner import Prisoner
import random

"""
Prisoner superclass
"""

class ChuckBass(Prisoner):

    """
    Constructor. Called once at the start of each match.
    If needed, override this method to initialize any 
    auxiliary data you want to use to determine your 
    Prisoner's strategy. This data will persist between
    rounds of a match but not between matches.
    """
#Esta estrategia comienza cooperando, pero si el oponente traiciona en algún momento, el jugador cambia gradualmente su comportamiento de la cooperación a la traición.
#Si el oponente traiciona en algún turno, el jugador ajusta gradualmente su probabilidad de cooperar hacia abajo utilizando factor_ajuste. Esto significa que el jugador se volverá menos propenso a cooperar a medida que el juego avance y el oponente traicione más.

    def __init__(self):
        self.cooperacion_actual = 0
        self.factor_ajuste = 0.1
        self.name = "Chuck Bass" # nombre completo a imprimir

    @staticmethod
    def name():
        return "Chuck Bass"

    """
    N : nro. total de rondas hasta ahora
    C : cantidad de veces que cooperé
    ci : nro. total de veces seguidas que cooperé
    eC : nro. total de veces que el (mismo) oponente cooperó
    """
    
    """
    Pick a strategy: return True to cooperate; return False to defect.
    If not overridden, the Prisoner will always cooperate.
    """
    def pick_strategy(self):
        
        probabilidad_cooperar = 1.0 - self.cooperacion_actual
        return 0.5 < probabilidad_cooperar
    
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
        if other_strategy is False:
            # Si el oponente traiciona, ajustar gradualmente hacia la traición
            self.cooperacion_actual += self.factor_ajuste
            # Asegurarse de que la probabilidad de cooperar esté en el rango [0, 1]
            self.cooperacion_actual = max(0, min(1, self.cooperacion_actual))
