from Prisoner import Prisoner
import random


class ReclusoFG():
    def __init__(self):
        self.name = "ReclusoFG"
        # Total de Partidas
        self.total = 0
        # Asumo que empieza confesando
        self.other_strategy = True

    @staticmethod
    def name():
        return "ReclusoFG"

    def pick_strategy(self):
        # Si es potencialmente la ultima jugada, disiento,
        # total el otro si hace Tit for tat deberia confesar
        if self.total % 100 == 99:
            return False
        else:
            # Despues de mi jugarreta, le doy changui
            if self.total % 100 == 1:
                return True
            else:
                # Si no, hago Tit for Tat
                if self.other_strategy == 1:
                    return True
                else:
                    return False

    def process_results(self, my_strategy, other_strategy):
        self.total += 1
        self.other_strategy = other_strategy
