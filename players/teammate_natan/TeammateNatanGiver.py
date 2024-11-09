from Prisoner import Prisoner
import random


class TeammateNatanGiver(Prisoner):

    def __init__(self):
        self.other_strategy = True  # asumo (arbitrariamente) que el oponente arranca cooperando
        self.name = "TeammateNatanGiver"  # nombre completo a imprimir
        self.perdonare = 0
        self.primeraVez = True
        self.valioLaPena = 0
        self.meCanse = False

        # AGREGAMOS PARA QUE SEA TEAMMATE
        self.code = [
            True, False, True, False, True, True, False, True, True, True,
            # True, True, False, True, False, True, True, False, False, True,
        ]
        self.code_state = 0

    @staticmethod
    def name():
        return "TeammateNatanGiver"

    def pick_strategy(self):
        if self.code_state == -1:
            return self.actual_pick_strategy()

        # si todavia estoy cambiando el codigo, hago eso
        if self.code_state < len(self.code):
            # todavia estoy viendo si es mi aliado
            return self.code[self.code_state]
        elif self.code_state == len(self.code):
            # es mi aliado
            return True

    def actual_pick_strategy(self):
        if self.meCanse: return False
        if self.other_strategy == True or self.perdonare > 0: return True

        if self.primeraVez or random.randint(1, 6) == 1:
            self.perdonare = 5

        self.primeraVez = False

        return self.perdonare > 0

    def process_results(self, my_strategy, other_strategy):
        if self.code_state == -1:
            # si no es mi aliado, proceso normal
            self.actual_process_result(my_strategy, other_strategy)

        elif self.code_state < len(self.code):
            # todavia estoy viendo si es mi aliado
            if other_strategy == self.code[self.code_state]:
                self.code_state = self.code_state + 1
            else:
                self.code_state = -1

        elif self.code_state == len(self.code):
            # si ya se que es mi aliado
            pass

    def actual_process_result(self, my_strategy, other_strategy):
        self.other_strategy = other_strategy

        if self.perdonare > 0:
            self.perdonare -= 1
            if other_strategy:
                self.valioLaPena += 1
            else:
                self.valioLaPena -= 1

        if self.perdonare == 0 and self.valioLaPena < 0:
            self.meCanse = True
