from Prisoner import Prisoner
import random


class Natan(Prisoner):

    def __init__(self):
        self.other_strategy = True  # asumo (arbitrariamente) que el oponente arranca cooperando
        self.name = "Natan"  # nombre completo a imprimir
        self.perdonare = 0
        self.primeraVez = True
        self.valioLaPena = 0
        self.meCanse = False

    @staticmethod
    def name():
        return "Natan"

    def pick_strategy(self):
        if self.meCanse: return False
        if self.other_strategy == True or self.perdonare > 0: return True

        if self.primeraVez or random.randint(1, 6) == 1:
            self.perdonare = 5

        self.primeraVez = False

        return self.perdonare > 0

    def process_results(self, my_strategy, other_strategy):
        self.other_strategy = other_strategy

        if self.perdonare > 0:
            self.perdonare -= 1
            if other_strategy:
                self.valioLaPena += 1
            else:
                self.valioLaPena -= 1

        if self.perdonare == 0 and self.valioLaPena < 0:
            self.meCanse = True
