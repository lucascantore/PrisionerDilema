from Prisoner import Prisoner


class TipForTat(Prisoner):

    def __init__(self):
        self.name = "TipForTat"  # nombre completo a imprimir
        self.next_strategy = True

    @staticmethod
    def name():
        return "TipForTat"

    # Esta función determina la estrategia a usar en cada ronda

    def pick_strategy(self):
        return self.next_strategy

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    def process_results(self, my_strategy, other_strategy):
        self.next_strategy = other_strategy
