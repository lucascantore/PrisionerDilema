from Prisoner import Prisoner
from random import random


class TobiCM(Prisoner):

    def __init__(self):
        self.name = "TobiCM"  # nombre completo a imprimir
        self._oponenteC = self._oponenteD = 0
        self._oponenteNoReacciona = self._oponenteTraiciona = 0
        self._estrategia = True  # empiezo cooperando
        self._estrategia_anterior = True  # empiezo cooperando

    @staticmethod
    def name():
        return "TobiCM"

    # Esta función determina la estrategia a usar en cada ronda, pudiendo mirar cualquier
    # atributo propio del objeto definido como jugador, en este caso ElGuason.

    def pick_strategy(self):
        return self._estrategia

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    # En este ejemplo, el prisionero sólo recordará la última estrategia del oponente. Si necesitan recordar más,
    # pueden hacerlo, incluso armar el historial (en una lista, tupla, diccionario, etc.)

    def process_results(self, my_strategy, other_strategy):
        # Recolecto datos
        if other_strategy:
            self._oponenteC += 1
            if not self._estrategia_anterior:
                self._oponenteNoReacciona += 1
        else:
            self._oponenteD += 1
            if self._estrategia_anterior:
                self._oponenteTraiciona += 1

        # Cambio estrategia
        self._estrategia_anterior = my_strategy
        if self._turnos() < 50:
            # Si no tengo suficientes datos del adversario: tit por tat
            self._estrategia = other_strategy
        elif self._oponenteNoReacciona > 0 and other_strategy:
            self._estrategia = False
        elif my_strategy and random() < 0.05:
            # tantear
            self._estrategia = False
        else:
            # default: tit for tat
            self._estrategia = other_strategy

    def _turnos(self):
        return self._oponenteC + self._oponenteD
