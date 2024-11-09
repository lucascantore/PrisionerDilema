from Prisoner import Prisoner  # importamos la clase padre
import random  # Solo lo usamos en el caso inicial.
import math # Solo lo usamos en el caso inicial.


class Zelig(Prisoner):

    def __init__(self):
        self.not_my_strat = (random.randint(0, math.floor(random.randint(10, 1000) * random.random()))) % 2
        self.name = "Zelig"

    @staticmethod
    def name():
        return "Zelig"

    def pick_strategy(self):
        return self.not_my_strat

    def process_results(self, my_strategy, other_strategy):
        self.not_my_strat = other_strategy

# La premisa de la "estrategia" es zonza, mi elección siempre va a ser la que el rival eligió en la ronda anterior.
# El término Zelig es referente a la pelicula homónima de Woody Allen.
# Referencia: https://www.imdb.com/title/tt0086637/

# Quizás no se amolda correctamente al personaje, en vez de actuar "como si fuera" el rival, es más bien un espejo de
# su último turno. Es decir, no necesariamente sabe adaptarse a cuál será la elección del rival en el próximo turno,
# sino que siempre queda al borde (i.e. el último turno).
