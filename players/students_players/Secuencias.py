# ESTRATEGIA DE SECUENCIAS, VARIACION JUSTA/RENCOROSA: intenta predecir el movimiento del otro jugador del siguiente modo: mira las últimas n jugadas, y se fija si
# esa sucesión de jugadas ya apareció antes. En ese caso, considera que el oponente va a jugar lo mismo que jugó después de la repetición más reciente de
# la secuencia de jugadas. Intenta mirar primero las secuencias de jugadas más largas posibles, con n descendiendo hasta 3. Para n menor a 3, consideramos que la
# secuencia no es lo suficientemente larga como para dar una predicción fiable, así que simplemente hace tit for tat.
# Luego, si predice que el oponente va a cooperar, y yo cooperé menos veces que el oponente,
# va a disentir con cierta probabilidad baja, para intentar "balancear" la cantidad de veces que cooperó cada jugador.
# Por otro lado, si predice que el oponente va a disentir, disiente como respuesta.

from Prisoner import Prisoner
import random


class SecuenciasJusta(Prisoner):

    def __init__(self):
        self.name = "SecuenciasJusta"  # nombre completo a imprimir
        self.list = []  # guarda una lista con todas las tuplas de movidas, ej [(False,True),(False,False),etc]
        self.turno = 0  # número de turno
        self.micoop = 0  # cantidad de veces que cooperé
        self.tucoop = 0  # cantidad de veces que cooperó el otro

    @staticmethod
    def name():
        return "SecuenciasJusta"

    def pick_strategy(self):
        if self.turno > 1:
            for n in range(self.turno - 1, 3,
                           -1):  # ultimasN será la lista de las últimas n movidas. n será la longitud de esta lista. minimo n = 3, porque las secuencias cortas parecerían menos significativas.
                ultimasN = self.list[-n:]
                for x in range(1, self.turno - n):
                    secAnterior = self.list[
                                  self.turno - x - n:self.turno - x]  # secAnterior son las secuencias de longitud n, previas a las últimas n movidas. Empieza mirando las secuencias más recientes
                    if secAnterior == ultimasN:
                        if self.list[n][1] == True and self.micoop < self.tucoop and random.randint(0, 10) >= 5:
                            return False
                        return self.list[n][1]
        if self.turno == 0:
            return True  # Empieza cooperando en el turno 0
        return self.list[self.turno - 1][
            1]  # en el turno 1, o si no encuentra una predicción con secuencias, se comporta como tit for tat.

    def process_results(self, my_strategy, other_strategy):
        self.list.append((my_strategy, other_strategy))
        self.turno = self.turno + 1
        if my_strategy == True:
            self.micoop = self.micoop + 1
        if other_strategy == True:
            self.tucoop = self.tucoop + 1
