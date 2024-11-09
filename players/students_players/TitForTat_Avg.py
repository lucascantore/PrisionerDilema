from Prisoner import Prisoner

"""
TitForTat_Avg: a Prisoner who copies their opponent's average choice.
"""
class TitForTat_Avg(Prisoner):
    
    def __init__(self):
        self.hist = []
        self.strat = True
        self.name = "TitForTat_Avg"

    @staticmethod
    def name():
        return "TitForTat_Avg"
    
    def pick_strategy(self):
        return self.strat
    
    def process_results(self, my_strategy, other_strategy):
        if other_strategy:
            self.hist.append(1)
        else:
            self.hist.append(-1)
        total = sum(self.hist)
        if total>=0:
            self.strat = True
        else:
            self.strat = False
