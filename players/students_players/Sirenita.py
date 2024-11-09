# Ejemplo

# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner
import random


# Sigue la declaración de la clase con su nombre, que tiene que ser subclase de Prisoner.
# Una instancia de la misma será el jugador, y las variables propias que usen deben ser todos atributos de self.

class Sirenita(Prisoner):

    # En __init__ va la inicialización que deseen, que se ejecutará antes de la "partida" 1
    # ante cada oponente; tener en cuenta que cuando pasan a competir con un nuevo oponente
    # se vuelve a ejecutar esta función, para arrancar desde 0.

    def __init__(self):
        self.name = "Sirenita"  # nombre completo a imprimir
        self.anterioresOtro = [True, False, False]
        self.anterioresOponente = [True, False, True, False]

    @staticmethod
    def name():
        return "Sirenita"

    """
    N : nro. total de rondas hasta ahora
    C : cantidad de veces que cooperé
    ci : nro. total de veces seguidas que cooperé
    eC : nro. total de veces que el (mismo) oponente cooperó
    """

    # Esta función determina la estrategia a usar en cada ronda, pudiendo mirar cualquier
    # atributo propio del objeto definido como jugador, en este caso ElGuason.

    def pick_strategy(self):
        for i in range(0, len(self.anterioresOponente) - 3):
            if (i == self.anterioresOtro[0] and i + 1 == self.anterioresOtro[1] and i + 2 == self.anterioresOtro[2]):
                otro = self.anterioresOponente[i + 3]
                if otro == True:
                    return False
                else:
                    r = random.randint(1, 10)
                    if r >= 7:
                        return False
                    return True
        r = random.randint(1, 20)
        if (r > 1):
            return False
        return True

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    # En este ejemplo, el prisionero sólo recordará la última estrategia del oponente. Si necesitan recordar más,
    # pueden hacerlo, incluso armar el historial (en una lista, tupla, diccionario, etc.)

    def process_results(self, my_strategy, other_strategy):
        (self.anterioresOponente).append(other_strategy)
        r = [self.anterioresOtro[1], self.anterioresOtro[2], other_strategy]
        self.anterioresOtro = r
