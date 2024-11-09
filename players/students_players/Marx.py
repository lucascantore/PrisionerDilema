from Prisoner import Prisoner
import random


class Marx(Prisoner):

    def __init__(self):
        self.N = self.C_seguidas = self.D_opponent_seguidas = 0
        self.other_strategy = True
        self.opponent_choices = [0, 0]  # en primera posicion #C - en segunda posicion #D
        self.name = "Marx"

    @staticmethod
    def name():
        return "Marx"

    """
    N : nro. total de rondas hasta ahora
    C_seguidas : nro. total de veces seguidas que cooperé
    D_seguidas : nor. total de veces seguidas que disenti
    opponent_choices : historial de elecciones del oponente
    """

    def pick_strategy(self):

        if self.N < 200:
            if self.C_seguidas == 1:
                return True

            if self.D_opponent_seguidas >= 3:
                r = random.randint(0, 9)
                if r == 9 and (self.opponent_choices[1] / self.N) < 0.7:
                    return True
                else:
                    return False

            return True

        else:
            r = random.randint(0, 2)
            if r == 2:
                return True
            else:
                return False

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy == True:
            self.C_seguidas += 1

        elif my_strategy == False:
            self.C_seguidas = 0

        self.other_strategy = other_strategy
        if other_strategy == True:
            self.D_opponent_seguidas = 0
            self.opponent_choices[0] += 1

        elif other_strategy == False:
            self.D_opponent_seguidas += 1
            self.opponent_choices[1] += 1
