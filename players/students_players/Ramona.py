#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:47:57 2023

@author: pablo
"""

# Ejemplo

# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner
import random


# Sigue la declaración de la clase con su nombre, que tiene que ser subclase de Prisoner.
# Una instancia de la misma será el jugador, y las variables propias que usen deben ser todos atributos de self.

class Ramona(Prisoner):

    # En __init__ va la inicialización que deseen, que se ejecutará antes de la "partida" 1
    # ante cada oponente; tener en cuenta que cuando pasan a competir con un nuevo oponente
    # se vuelve a ejecutar esta función, para arrancar desde 0.

    def __init__(self):
        self.N = self.C = self.ci = self.di = 0  # inicializo los totales
        self.eC = 0
        self.other_strategy = True  # asumo (arbitrariamente) que el oponente arranca cooperando
        self.name = "Ramona"  # nombre completo a imprimir
        self.ss = 0
        self.interes = True

    @staticmethod
    def name():
        return "Ramona"

    """
    N : nro. total de rondas hasta ahora
    C : cantidad de veces que cooperé
    ci : nro. total de veces seguidas que cooperé
    eC : nro. total de veces que el (mismo) oponente cooperó
    """

    # Esta función determina la estrategia a usar en cada ronda, pudiendo mirar cualquier
    # atributo propio del objeto definido como jugador, en este caso ElGuason.

    def pick_strategy(self):

        if (self.N // 40 == 0):
            self.interes = (self.ss > 0)
            self.ss = 0

        brackets = [20, 40, 80, 160, 320, 800]

        if self.N < brackets[0]:
            return self.other_strategy

        elif self.N < brackets[1]:
            if (self.N == brackets[0]):
                self.interes = (self.ss > 0)
                self.ss = 0
            return (self.C <= self.eC)

        elif self.N < brackets[2] and self.interes:
            if self.other_strategy and self.ci <= 3:  # y cooperé muchas veces en total
                return True
            else:
                return False
            r = random.randint(0, 2)
            if r == 0:
                return True
            else:
                return False

        elif self.N < brackets[3] and self.interes:

            r = random.randint(0, self.N ^ 2)
            return (r < self.N)

        elif self.N < brackets[4] and self.interes:

            return self.other_strategy

        elif self.N < brackets[5] and self.interes:

            r = random.randint(0, self.di)

            l = self.N - brackets[2] // 10

            if self.other_strategy and r > l:
                return True
            else:
                return False
        else:
            return False

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    # En este ejemplo, el prisionero sólo recordará la última estrategia del oponente. Si necesitan recordar más,
    # pueden hacerlo, incluso armar el historial (en una lista, tupla, diccionario, etc.)

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy == True:  # si la última vez cooperé, decido cooperar
            self.C += 1  # incremento la cantidad total de veces que cooperé
            self.ci += 1  # y la cantidad de veces seguidas que cooperé
            self.di = 0

        elif my_strategy == False:  # en caso contrario
            self.ci = 0  # pongo en 0 la cantidad de veces seguidas que cooperé
            self.di += 1

        self.other_strategy = other_strategy  # actualizo la última estrategia del oponente con la actual
        if other_strategy == True:  # si el oponente la última vez cooperó
            self.eC += 1  # incremento la cantidad total de veces que cooperó
            self.ss += 1
