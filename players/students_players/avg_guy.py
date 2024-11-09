
from Prisoner import Prisoner
import random

class AvgGuy(Prisoner):

    name="average_guy"

    def __init__(self):
        self.other_d = self.other_c = 0
        self.n = 0
        self.first_game = True
        self.name = "AvgGuy"

    @staticmethod
    def name():
        return "AvgGuy"

    """
    other_d:    total de denegadas del contrincante
    other_c:    total de cooperadas del contrincante
    n:          total de jugadas
    first_game: si es la primer jugada o no
    """

    def pick_strategy(self):
        if self.first_game:
            return False # Es malo por default
            # (parece ganarle siempre al guasón y varias veces a evil_guy)
        else:
            if self.other_c / self.n >= 0.8:
                return True

    def process_results(self, my_strategy, other_strategy):
        self.n += 1
        if other_strategy:
            self.other_c += 1
        else:
            self.other_d += 1
        
