from Prisoner import Prisoner
from random import choices


class Judas(Prisoner):

    def __init__(self):
        self.betray = 5
        self.other_strategy = True
        self.name = "Judas"

    @staticmethod
    def name():
        return "Judas"

    # Repite la estrategia previa del contrario, con una probabilidad del 5% de traicionarlo si eligió cooperar

    def pick_strategy(self):
        if self.other_strategy:
            return choices([False, True], cum_weights=(self.betray, 100))
        else:
            return False

    def process_results(self, _, other_strategy):
        self.other_strategy = other_strategy
