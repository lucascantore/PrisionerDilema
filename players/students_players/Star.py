from Prisoner import Prisoner
from random import randint


class Star(Prisoner):
    def __init__(self):
        self.N = self.C = self.ci = 0
        self.eC = 0
        self.other_strategy = False
        self.name = "Star"

    @staticmethod
    def name():
        return "Star"

    def pick_strategy(self):
        return False

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        my_strategy == False  # en caso contrario
        self.other_strategy = other_strategy  # actualizo la última estrategia del oponente con la actual
        if other_strategy == True:  # si el oponente la última vez cooperó
            self.eC += 1  # incremento la cantidad total de veces que cooperó
