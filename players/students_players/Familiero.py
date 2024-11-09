"""
Prisoner superclass
- A traves de lo dado en esta Subclase crear una estrategia personal para un torneo en clase
"""

from Prisoner import Prisoner
import random


# ------------------------------------------------------------------------------#

class Familiero(Prisoner):
    """
    Constructor. Called once at the start of each match.
    If needed, override this method to initialize any 
    auxiliary data you want to use to determine your 
    Prisoner's strategy. This data will persist between
    rounds of a match but not between matches.
    """

    def __init__(self):
        self.eD = self.ci = 0
        self.r = random.randint(0, 1000)
        self.other_strategy = True  # asumo que el contrincante comenzara cooperando
        self.name = "Familiero"  # nombre completo a imprimir

    @staticmethod
    def name():
        return "Familiero"

    """
    N : nro. total de rondas hasta ahora
    ci : nro. total de veces seguidas que cooperé
    eD : nro. total de veces seguidas que el oponente no cooperó
    other_strategy : me guardo el tipo de jugabilidad que esta teniendo el contrincante
    """

    """
    Pick a strategy: return True to cooperate; return False to defect.
    If not overridden, the Prisoner will always cooperate.
    """

    def pick_strategy(self):

        if self.other_strategy == False:  # si el contrincante no coopera, yo no coopero
            return False
        else:
            if self.ci > 2:  # si coopero muchas veces seguidas no coopero
                return False
            else:
                for i in range(2, int(self.r / 2)):  # no coopera en los numeros primos
                    if (self.r % i) == 0:
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

        self.r += 1

        if my_strategy == True:
            self.ci += 1
        else:
            self.ci = 0

        if other_strategy == False:
            if self.eD < 2:
                self.eD += 1
            else:
                self.other_strategy = False
        else:
            if self.eD > 0:
                self.eD -= 1
            else:
                self.other_strategy = True

# ------------------------------------------------------------------------------#
