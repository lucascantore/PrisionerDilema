# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner
import random


class PrisioneroNY(Prisoner):

    def __init__(self):
        self.N = self.C = self.eC = self.ci = self.eci = 0  # inicializo los totales
        self.other_strategy = True  # asumo (arbitrariamente) que el oponente arranca cooperando
        self.name = "PrisioneroNY"  # nombre completo a imprimir

    @staticmethod
    def name():
        return "PrisioneroNY"

    """
    N : nro. total de rondas hasta ahora
    C : cantidad de veces que cooperé
    ci : nro. total de veces seguidas que cooperé
    eC : nro. total de veces que el (mismo) oponente cooperó
    """

    def pick_strategy(self):
        # Si cooperé seguido más que la mitad de las veces que coopere en la partida
        if self.ci > self.C / 2:
            # Si el oponente coopero menos que yo seguidamente
            if self.eci < self.ci:
                return False  # Decido no cooperar
            return self.other_strategy  # Sino repito la jugada anterior del otro
        else:
            # Calculo el promedio (con N incrementado)
            cMean = self.C / (self.N + 1)
            ecMean = self.eC / (self.N + 1)
            # Si el oponente es más propenso a no cooperar que yo
            if ecMean <= cMean:
                # Al azar, con probabilidad 0.5, decido si no cooperar (desconfío)
                return not (random.randint(0, 9) < 5)
            else:
                return True  # Sigo cooperando (me hago más propenso a cooperar)

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy == True:  # si la última vez cooperé
            self.C += 1  # incremento la cantidad total de veces que cooperé
            self.ci += 1  # y la cantidad de veces seguidas que cooperé

        elif my_strategy == False:  # en caso contrario
            self.ci = 0  # pongo en 0 la cantidad de veces seguidas que cooperé

        self.other_strategy = other_strategy  # actualizo la última estrategia del oponente con la actual
        if other_strategy == True:  # si el oponente la última vez cooperó
            self.eC += 1  # incremento la cantidad total de veces que cooperó
            self.eci += 1  # incremento la cantidad total de veces que cooperó seguidas
        else:
            self.eci = 0  # pongo en 0 la cantidad de veces seguidas que cooperé
