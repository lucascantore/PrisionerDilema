# Ejemplo

# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner
import random


# Sigue la declaración de la clase con su nombre, que tiene que ser subclase de Prisoner.
# Una instancia de la misma será el jugador, y las variables propias que usen deben ser todos atributos de self.

class E_tit_for_2_tat(Prisoner):

    # En __init__ va la inicialización que deseen, que se ejecutará antes de la "partida" 1
    # ante cada oponente; tener en cuenta que cuando pasan a competir con un nuevo oponente
    # se vuelve a ejecutar esta función, para arrancar desde 0.

    def __init__(self):
        self.Cantidad_de_partidas = self.cantidad_de_no_cooperadas_rival = self.cantidad_de_no_cooperadas_seguidas = self.cantidad_de_venganza = 0  # inicializo los totales
        self.other_strategy = True  # asumo (arbitrariamente) que el oponente arranca cooperando
        self.name = "E-Tit-for-2-tat"  # nombre completo a imprimir
        self.segunda_oportunidad = True
        self.venganza = False

    @staticmethod
    def name():
        return "E-Tit-for-2-tat"

    # Esta función determina la estrategia a usar en cada ronda, pudiendo mirar cualquier
    # atributo propio del objeto definido como jugador, en este caso ElGuason.

    def pick_strategy(self):
        if self.venganza:
            if self.cantidad_de_no_cooperadas_seguidas < self.cantidad_de_venganza:
                return False
            else:
                self.venganza = False
                return False
        else:
            return True

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    # En este ejemplo, el prisionero sólo recordará la última estrategia del oponente. Si necesitan recordar más,
    # pueden hacerlo, incluso armar el historial (en una lista, tupla, diccionario, etc.)

    def process_results(self, my_strategy, other_strategy):
        if my_strategy == True:
            self.cantidad_de_no_cooperadas_seguidas = 0

        elif my_strategy == False:
            self.cantidad_de_no_cooperadas_seguidas += 1

        self.other_strategy = other_strategy  # actualizo la última estrategia del oponente con la actual
        if other_strategy == False and my_strategy == True:  # si el oponente la última vez no cooperó
            self.cantidad_de_no_cooperadas_rival += 1  # incremento la cantidad total de veces que no cooperó
            if self.segunda_oportunidad:
                self.segunda_oportunidad = False
            else:
                self.cantidad_de_venganza = int(2 ** (self.cantidad_de_no_cooperadas_rival / 2))
                # print(f"Venganza llego a {self.cantidad_de_venganza}")
                # print(f"Cuando el rival {self.cantidad_de_no_cooperadas_rival}")
                self.venganza = True
                self.segunda_oportunidad = True
