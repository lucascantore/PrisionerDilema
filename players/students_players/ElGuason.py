# Ejemplo

# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner
import random


# Sigue la declaración de la clase con su nombre, que tiene que ser subclase de Prisoner.
# Una instancia de la misma será el jugador, y las variables propias que usen deben ser todos atributos de self.

class ElGuason(Prisoner):

    # En __init__ va la inicialización que deseen, que se ejecutará antes de la "partida" 1
    # ante cada oponente; tener en cuenta que cuando pasan a competir con un nuevo oponente
    # se vuelve a ejecutar esta función, para arrancar desde 0.

    def __init__(self):
        self.N = self.C = self.ci = 0  # inicializo los totales
        self.eC = self.eD = 0
        self.other_strategy = True  # asumo (arbitrariamente) que el oponente arranca cooperando
        self.name = "prisonBreaker"  # nombre completo a imprimir
        self.historyOfStrategies = []  ## historial de las estrategias en la forma (mia, rival)

    @staticmethod
    def name():
        return "prisonBreaker"

    """
    N : nro. total de rondas hasta ahora
    C : cantidad de veces que cooperé
    ci : nro. total de veces seguidas que cooperé
    eC : nro. total de veces que el (mismo) oponente cooperó
    eD : nro. total de veces que el (mismo) oponente no cooperó
    """

    # Esta función determina la estrategia a usar en cada ronda, pudiendo mirar cualquier
    # atributo propio del objeto definido como jugador, en este caso ElGuason.

    def pick_strategy(self):

        # if self.ci > 2: # si cooperé muchas veces seguidas
        #     if self.C/self.N > 0.5: # y cooperé muchas veces en total
        #         return False # disiente
        #     else:
        #         return True # coopera
        #
        # else:
        #     r = random.randint(0,9) # genera un número aleatorio de 0 a 9
        #     if r < 4: # esta proporción de veces
        #         return self.other_strategy # hago la última estrategia del oponente
        #     else:
        #         return True # coopero

        # Generous TFT modified
        # ---------------------

        if self.N == 0:
            return True
        else:

            # A little modification to GTFT for mislead the oponent
            if self.N % 100 == 0 or self.N % 101 == 0:
                if random.random() < 0.5:
                    return True
                else:
                    return False

            lastMove = self.historyOfStrategies[self.N - 1]
            lastMove_oponent = lastMove[1]

            if lastMove_oponent == False:
                # Occasionally cooperate even if the opponent has defected in the past
                if random.random() < 0.2:
                    return True
                else:
                    return False
            else:
                return False

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy == True:  # si la última vez cooperé, decido cooperar
            self.C += 1  # incremento la cantidad total de veces que cooperé
            self.ci += 1  # y la cantidad de veces seguidas que cooperé

        elif my_strategy == False:  # en caso contrario
            self.ci = 0  # pongo en 0 la cantidad de veces seguidas que cooperé

        self.other_strategy = other_strategy  # actualizo la última estrategia del oponente con la actual
        if other_strategy == True:  # si el oponente la última vez cooperó
            self.eC += 1  # incremento la cantidad total de veces que cooperó
        else:
            self.eD += 1  # sino, incremento la cantidad total de veces que no cooperó

        self.historyOfStrategies.append((my_strategy, other_strategy))
