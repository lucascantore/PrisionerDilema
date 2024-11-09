from Prisoner import Prisoner
import random

class Ilan(Prisoner):
    def __init__(self):
        self.last_my_strategy = False
        self.last_other_strategy = False
        self.name = "Ilan"

    @staticmethod
    def name():
        return "Ilan"

    def pick_strategy(self):
        if not self.last_my_strategy and not self.last_other_strategy: return False
        if random.randint(0,9) < 4: return False
        return True

    def process_results(self, my_strategy, other_strategy):
        self.last_my_strategy = my_strategy
        self.last_other_strategy = other_strategy
