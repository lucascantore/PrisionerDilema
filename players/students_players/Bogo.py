from Prisoner import Prisoner
import random

class Bogo(Prisoner):
    def __init__(self):
        self.name = "Bogo"

    @staticmethod
    def name():
        return "Bogo"
    
    def pick_strategy(self):
        return random.randint(0,2) == 0
