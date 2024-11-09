from Prisoner import Prisoner


class Gaston(Prisoner):
    def __init__(self):
        """
        N : nro. total de rondas hasta ahora
        C : cantidad de veces que cooperé
        ci : nro. total de veces seguidas que cooperé
        eC : nro. total de veces que el (mismo) oponente cooperó
        """
        self.N = self.C = self.ci = self.eC = 0
        self.other_strategy = True # asumo (arbitrariamente) que el oponente arranca cooperando
        self.name = "Gaston"

    @staticmethod
    def name():
        return "Gaston"


    def pick_strategy(self):
        cooperate_every_10_rounds = (self.N % 10 == 0)
        return cooperate_every_10_rounds
    
    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy == True:     # si cooperé
            self.C += 1             # incremento la cantidad total de veces que cooperé
            self.ci += 1            # y la cantidad de veces seguidas que cooperé

        elif my_strategy == False:  # si no cooperé
            self.ci = 0             # pongo en 0 la cantidad de veces seguidas que cooperé

        self.other_strategy = other_strategy    # actualizo la última estrategia del oponente con la actual
        if other_strategy == True:              # si el oponente la última vez cooperó
            self.eC += 1                        # incremento la cantidad total de veces que cooperó
