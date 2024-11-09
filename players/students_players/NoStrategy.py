from Prisoner import Prisoner
import random


class NoStrategy(Prisoner):
    def __init__(self):
        self.rand = random.randint(1, 10)
        self.other_strategy = random.randint(0, 1) == 0
        self.name = "NoStrategy"

    @staticmethod
    def name():
        return "NoStrategy"

    def pick_strategy(self):
        if self.rand == 0:
            self.rand = random.randint(1, 10)
            self.other_strategy = random.randint(0, 1) == 0
        else:
            self.rand -= 1

        return self.other_strategy

    def process_results(self, my_strategy, other_strategy):
        pass
