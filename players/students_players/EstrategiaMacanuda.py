
from Prisoner import Prisoner

class EstrategiaMacanuda(Prisoner):

    def __init__(self):
        self.state = 0
        self.name="EstrategiaMacanuda" # nombre completo a imprimir

    @staticmethod
    def name():
        return "EstrategiaMacanuda"

    def pick_strategy(self):
        
        if self.state < 7:
            return True
        else:
            return False

    def process_results(self, my_strategy, other_strategy):
        
        if self.state < 6:
            if other_strategy:
                self.state += 1
            else:
                self.state = 8
        elif self.state == 6:
            self.state = 12
        elif self.state == 12:
            self.state = 0
        else:
            if other_strategy:
                self.state = 0
            else:
                self.state += 1
