from Prisoner import Prisoner


class Lucifer(Prisoner):

    def __init__(self):
        self.name = "Lucifer"  # nombre completo a imprimir

    # Esta función determina la estrategia a usar en cada ronda

    def pick_strategy(self):
        return False

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    def process_results(self, my_strategy, other_strategy):
        pass
