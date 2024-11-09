# Ejemplo

# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner
import random


# Sigue la declaración de la clase con su nombre, que tiene que ser subclase de Prisoner.
# Una instancia de la misma será el jugador, y las variables propias que usen deben ser todos atributos de self.

class RolDeCanela(Prisoner):

    # En __init__ va la inicialización que deseen, que se ejecutará antes de la "partida" 1
    # ante cada oponente; tener en cuenta que cuando pasan a competir con un nuevo oponente
    # se vuelve a ejecutar esta función, para arrancar desde 0.

    def __init__(self, deadlock_threshold: int = 3, randomness_threshold: int = 8):
        self.deadlock_threshold = deadlock_threshold
        self.randomness_threshold = randomness_threshold
        self.randomness_counter = 0
        self.deadlock_counter = 0
        self.N = 0
        self.opponent_move = True
        self.opponent_previous_move = True
        self.move = True
        self.name = "RolDeCanela"

    @staticmethod
    def name():
        return "RolDeCanela"

    # deadlock_threshold : umbral para deadlock

    # randomness_threshold : umbral para aleatoriedad
    # randomness_counter : contador para aleatoriedad
    # deadlock_counter : contador para deadlock
    # N : cantidad de rondas jugadas
    # opponent_move : ultima jugada de mi oponente
    # opponent_previous_move : jugada anterior de mi oponente
    # move : ultima jugada mia

    # Esta función determina la estrategia a usar en cada ronda, pudiendo mirar cualquier
    # atributo propio del objeto definido como jugador, en este caso ElGuason.

    def pick_strategy(self):

        # arranco coperando
        if self.N == 0:
            return True

        # en la segunda ronda aplico TFT
        if self.N == 1:
            return self.opponent_move

        # estamos en un deadlock, entonces coopero para romperlo
        if self.deadlock_counter >= self.deadlock_threshold:
            move = True
            if self.deadlock_counter == self.deadlock_threshold:
                self.deadlock_counter = self.deadlock_threshold + 1
            else:
                self.deadlock_counter = 0

        else:
            # si el oponente viene cooperando, decremento randomness
            if self.opponent_move == True & self.opponent_previous_move == True:
                self.randomness_counter -= 1
            # si el oponente cambio de movimineto, incremento
            if self.opponent_move != self.opponent_previous_move:
                self.randomness_counter += 1
            # si el oponente hizo algo distinto a mi, incremento
            if self.move != self.opponent_move:
                self.randomness_counter += 1
            # si randomness_counter no esta en el threshold, dejo de cooperar
            if self.randomness_counter >= self.randomness_threshold:
                move = False
            else:
                # TFT
                move = self.opponent_move
                # vemos si hay deadlock
                if self.opponent_move != self.opponent_previous_move:
                    self.deadlock_counter += 1
                else:
                    self.deadlock_counter = 0
        return move

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    # En este ejemplo, el prisionero sólo recordará la última estrategia del oponente. Si necesitan recordar más,
    # pueden hacerlo, incluso armar el historial (en una lista, tupla, diccionario, etc.)

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        self.move = my_strategy
        self.opponent_previous_move = self.opponent_move
        self.opponent_move = other_strategy
