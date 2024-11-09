from Prisoner import Prisoner
import random

"""
Recordar que los posibles resultados para el primer jugador del Dilema del Prisionero son
(D,D) → 0
(C,C) → 1
(D,C) → 2
(C,D) → -1
En este juego, los representamos como pares de bool. C = True, D = False
"""

"""
Parámetros de Roberto
n = numero de rondas
d = numero de D seguidas
oc = numero de C seguidas del oponente
"""


class Roberto(Prisoner):
    def __init__(self):
        self.name = "Roberto"
        self.n = 0
        self.d = 0
        self.oc = 0
        self.od = 0
        self.eps = (-1 / 20, 0, 1 / 20)

    @staticmethod
    def name():
        return "Roberto"

    def pick_strategy(self):
        """
    Estrategia de Roberto. Es un prisionero que tiende a elegir D, pero cada vez que elige D
    aumenta en la probabilidad de que elija C. Así mismo, que el oponente elija C tambien aumenta
    la probabilidad de que Roberto elija C. Para que no esté siempre determinado por las jugadas previas,
    sumamos una variable aleatoria eps de valores posibles {-1/20, 0, 1/20}
    La fórmula que usamos para la probabilidad p = min{1, d/10 + oc/5 + eps} de devolver C
    Además, si el oponente va al menos 20 rondas seguidas sin confesar, Roberto siempre devuelve False.
    """
        if self.od >= 20:
            return False
        else:
            p = min(1, self.d / 10 + self.oc / 5 + random.choice(self.eps))
            return random.random() < p

    def process_results(self, my_strategy, other_strategy):
        self.n += 1
        if my_strategy == True:
            self.d = 0
        else:
            self.d += 1

        if other_strategy == True:
            self.oc += 1
            self.od = 0
        else:
            self.oc = 0
            self.od += 1
