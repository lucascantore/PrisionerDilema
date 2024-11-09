from Prisoner import Prisoner
import random
from collections import deque


#
# Lautaro Serpa Lu:1128/21    Matias Gerpe Lizarraga Lu:870/21
#

class Xerpa(Prisoner):

    def __init__(self):
        self.N = 1  # inicializo los totales
        self.op_recentC = 0
        self.op_numberOfD = 0
        self.name = "Xerpa"  # nombre completo a imprimir
        self.recentPlays = deque([])

    @staticmethod
    def name():
        return "Xerpa"

    def pick_strategy(self):
        # invitar a cooperar
        if self.N <= 10:
            return True

        # vamos a utilizar azar para ser poco predeciblesle
        random_num = random.randint(1, 10)

        # luego de observar al adversario empezamos a adaptar la estrategia
        if (self.N > 20):
            # nos sacamos este caso
            if (self.op_numberOfD >= self.N - 1):
                return False

            # si no estamos cooperando nada, invitamos cada tanto a la cooperacion
            if (self.op_recentC < 1):
                if (random_num > 4):
                    return True

            # si estamos cooperando mucho, traicionamos un poco para rascar puntos (queremos salir primeros)
            if (self.op_recentC > 8):
                if (random_num > 5):
                    return False

        # si coopera, cooperamos. Si no, no. Pero somos poco predecibles
        if (random_num <= self.op_recentC):
            return True
        else:
            return False

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        self.recentPlays.append(other_strategy)
        if other_strategy == False: self.op_numberOfD += 1
        if (self.N <= 10):
            self.op_recentC += other_strategy
        else:
            old_Strategy = self.recentPlays.popleft()
            if (other_strategy == False):
                if old_Strategy == True:
                    self.op_recentC += -1
            else:
                if old_Strategy == False:
                    self.op_recentC += 1
