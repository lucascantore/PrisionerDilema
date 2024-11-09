# Ejemplo

# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner
import random


# Sigue la declaración de la clase con su nombre, que tiene que ser subclase de Prisoner.
# Una instancia de la misma será el jugador, y las variables propias que usen deben ser todos atributos de self.

class TrustMe(Prisoner):

    # En __init__ va la inicialización que deseen, que se ejecutará antes de la "partida" 1
    # ante cada oponente; tener en cuenta que cuando pasan a competir con un nuevo oponente
    # se vuelve a ejecutar esta función, para arrancar desde 0.

    def __init__(self):
        self.N = self.C = self.ci = 0  # inicializo los totales
        self.eC = 0
        self.eNaive = 0
        self.other_strategy = False
        self.name = "TrustMe"  # nombre completo a imprimir

    @staticmethod
    def name():
        return "TrustMe"

    """
    N : nro. total de rondas hasta ahora
    C : cantidad de veces que cooperé
    ci : nro. total de veces seguidas que cooperé
    eC : nro. total de veces que el (mismo) oponente cooperó
    eNaive: nro. total de veces seguidas que el oponento cooperó
    """

    # Esta función determina la estrategia a usar en cada ronda, pudiendo mirar cualquier
    # atributo propio del objeto definido como jugador, en este caso ElGuason.

    def pick_strategy(self):
        # La idea es cooperar las primeras rondas para ganar un poco la confianza del oponente, y luego dejar de cooperar
        # Si se nota que el oponente coopera muchas rondas seguidas, se coopera una vez para mantener un poco la confianza
        if self.C <= 20:
            return True
        if self.eNaive > 3:
            self.eNaive = 0
            return True
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

        elif my_strategy == False:  # en caso contrario
            self.ci = 0  # pongo en 0 la cantidad de veces seguidas que cooperé

        self.other_strategy = other_strategy  # actualizo la última estrategia del oponente con la actual
        if other_strategy == True:  # si el oponente la última vez cooperó
            self.eC += 1  # incremento la cantidad total de veces que cooperó
            self.eNaive += 1  # cuento la cantidad de veces seguidas que cooperó el enemigo
        elif other_strategy == False:
            self.eNaive = 0
