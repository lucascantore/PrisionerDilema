# Ejemplo

# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner
import random


# Sigue la declaración de la clase con su nombre, que tiene que ser subclase de Prisoner.
# Una instancia de la misma será el jugador, y las variables propias que usen deben ser todos atributos de self.

class MateConNueces(Prisoner):

    # En __init__ va la inicialización que deseen, que se ejecutará antes de la "partida" 1
    # ante cada oponente; tener en cuenta que cuando pasan a competir con un nuevo oponente
    # se vuelve a ejecutar esta función, para arrancar desde 0.

    def __init__(self):
        self.N = 2
        self.prob_C = 0.5
        self.prob_D = 0.5
        self.C = 1
        self.D = 1
        self.name = "MateConNueces"

    @staticmethod
    def name():
        return "MateConNueces"

    # Esta función determina la estrategia a usar en cada ronda, pudiendo mirar cualquier
    # atributo propio del objeto definido como jugador, en este caso ElGuason.

    def pick_strategy(self):
        p = random.uniform(0, 1)
        randomChange = random.uniform(0, 1)
        confese = True if p < self.prob_C else False
        if randomChange > max(self.prob_D, self.prob_C):
            confese = not confese
        return confese

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    # En este ejemplo, el prisionero sólo recordará la última estrategia del oponente. Si necesitan recordar más,
    # pueden hacerlo, incluso armar el historial (en una lista, tupla, diccionario, etc.)

    def process_results(self, my_strategy, other_strategy):
        if my_strategy and other_strategy:  # Empate
            self.D += 1
        elif not my_strategy and other_strategy:  # Gane
            self.C += 1
        elif my_strategy and not other_strategy:  # Perdi
            self.D += 1
        else:  # Empate
            self.C += 1
        self.N += 1
        self.prob_C = self.C / self.N
        self.prob_D = self.D / self.N
