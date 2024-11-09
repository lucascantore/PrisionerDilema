from Prisoner import Prisoner


# import random

class Sebastian(Prisoner):
    def __init__(self):
        self.historial_yo = self.historial_adversario = []
        self.coop_yo = self.coop_adversario = 0
        self.name = "Sebastian"  # nombre completo a imprimir

    @staticmethod
    def name():
        return "Sebastian"

    def pick_strategy(self):
        cociente = self.coop_yo / (self.coop_adversario + 1)
        if cociente > 1.15:  # Estoy cooperando mucho mas que el otro
            return False
        elif cociente < 0.85:  # Estoy cooperando mucho menos que el otro
            return True
        else:  # En otro caso tit for tat
            try:
                return self.historial_adversario[-1]
            except:
                return True

    def process_results(self, my_strategy, other_strategy):
        self.coop_yo += my_strategy
        self.coop_adversario += other_strategy
        self.historial_yo.append(my_strategy)
        self.historial_adversario.append(other_strategy)
