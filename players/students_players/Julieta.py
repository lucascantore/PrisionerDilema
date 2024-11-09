from Prisoner import Prisoner
import random


class Julieta(Prisoner):

    def __init__(self):
        self.N = 0  # N = nro total de rondas hasta ahora
        self.eC = 0  # eC = nro total de veces que el oponente cooperó
        self.name = "Julieta"  # nombre completo a imprimir

    @staticmethod
    def name():
        return "Julieta"

    def pick_strategy(self):
        if self.eC == 0:
            return False
        else:
            dame_numero = random.randint(0, self.N)
            if dame_numero < (self.eC // 2):
                return True
            else:
                return False

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if other_strategy == True:  # si el oponente la última vez cooperó
            self.eC += 1  # incremento la cantidad total de veces que cooperó
