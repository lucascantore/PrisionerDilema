from Prisoner import Prisoner
from random import random


class Pablo(Prisoner):

    def __init__(self):
        self.name = 'Pablo'
        self.strategy = True
        self.noise_probability = 0.09

    @staticmethod
    def name():
        return "Pablo"

    def pick_strategy(self):
        if random() < self.noise_probability:
            return not self.strategy
        return self.strategy

    def process_results(self, my_strategy, other_strategy):
        if my_strategy == other_strategy:
            self.strategy = my_strategy
        else:
            self.strategy = not my_strategy
