from Prisoner import Prisoner
import random


class JugaCporfa(Prisoner):

    def __init__(self):
        self.opponentconsent = []
        self.name = "JugaCporfa"

    @staticmethod
    def name():
        return "JugaCporfa"


    def pick_strategy(self):
        if len(self.opponentconsent)<5:
            return True
        count = 0
        for strat in self.opponentconsent[:-6:-1]:
            if strat: count+=1
        if count >= 4: return True
        return False


    def process_results(self, my_strategy, other_strategy):
        self.opponentconsent.append(other_strategy)
