from Prisoner import Prisoner
import random

class IAndOTitForTat(Prisoner):
    def __init__(self):
        self.other_strategy = True # asumo (arbitrariamente) que el oponente arranca cooperando
        self.other_penultimate_strategy = True
        self.name="IAndOTitForTat"
        self.strategies = []

    @staticmethod
    def name():
        return "IAndOTitForTat"

    DEFECT_AGAIN_PROB = 0.75
    COOPERATE_ANYWAY_PROB = 0.10

    def pick_strategy(self):
        rand = random.random()
        if self.other_penultimate_strategy and self.other_strategy and rand < self.DEFECT_AGAIN_PROB:
            return False
        elif not self.other_strategy and rand < self.COOPERATE_ANYWAY_PROB:
            return True
        else:
            
            amount_both_cooperated = self.strategies.count((True, True))
            amount_betrayed = self.strategies.count((True, False))
            amount_betrayed_other = self.strategies.count((False, True))

            mostly_cooperation = amount_both_cooperated > amount_betrayed and amount_both_cooperated > amount_betrayed_other

            if mostly_cooperation:
                return True
            else:
                return False

    def process_results(self, my_strategy, other_strategy):
        self.other_strategy = other_strategy
        self.strategies.append((my_strategy, other_strategy))
    
    def opponent_cooperated(self, other_strategy):
        return other_strategy
    
    def opponent_defected(self, other_strategy):
        return not other_strategy
