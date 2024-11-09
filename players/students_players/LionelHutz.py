# Lionel Hutz, abogado, se vió involucrado en un crimen y busca reducir su condena a su coautor.

from Prisoner import Prisoner
import random

class LionelHutz(Prisoner):
    def __init__(self):
        self.N = 0
        self.other_strategy = True
        self.name = "Lionel Hutz"

    @staticmethod
    def name():
        return "Lionel Hutz"
        
    def pick_strategy(self):
        r = random.randint(5,12)
        if (not self.other_strategy): return False
        else: return (not self.N % r == 0)

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        self.other_strategy = other_strategy