import random
from Prisoner import Prisoner

class TitForTatConRandom(Prisoner):
    def __init__(self):
        self.N = 0  # Número de jugadas realizadas
        self.other_strategy = True  # Asumimos que el oponente arranca cooperando
        self.name = "TitForTatConRandom"
        self.random_every = 7  # Cada 7 rondas, jugamos de forma aleatoria

    @staticmethod
    def name():
        return "TitForTatConRandom"

    def pick_strategy(self):
        if self.N > 0 and self.N % self.random_every == 0:
            # Cada 7 jugadas, elegimos al azar
            return random.choice([True, False])
        else:
            # En las demás jugadas, seguimos con Tit for Tat
            return self.other_strategy

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        self.other_strategy = other_strategy
