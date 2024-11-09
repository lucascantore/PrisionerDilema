from Prisoner import Prisoner
from random import randint


class Lucy(Prisoner):
    def __init__(self):
        self.N = self.C = self.ci = 0
        self.eC = 0
        self.other_strategy = False
        self.name = "Lucy"

    @staticmethod
    def name():
        return "Lucy"

    def pick_strategy(self):
        if not self.other_strategy:
            return False
        elif self.eC / self.N > 0.564:
            return True
        else:
            return False

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        my_strategy == False  # en caso contrario
        self.other_strategy = other_strategy  # actualizo la última estrategia del oponente con la actual
        if other_strategy == True:  # si el oponente la última vez cooperó
            self.eC += 1  # incremento la cantidad total de veces que cooperó
