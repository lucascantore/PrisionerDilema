from Prisoner import Prisoner


class TeammateLuciferPointGiver(Prisoner):

    def __init__(self):
        self.name = "TeammateLuciferPointGiver"  # nombre completo a imprimir
        self.code = [
            True, True, False, False, False, True, True, False, True, True,
            # True, False, True, False, True, True, False, True, True, True
        ]
        self.code_state = 0

    @staticmethod
    def name():
        return "TeammateLuciferPointGiver"

    # Esta función determina la estrategia a usar en cada ronda

    def pick_strategy(self):
        strategy = False

        if self.code_state == -1:
            strategy = False

        elif self.code_state < len(self.code):
            # todavia estoy viendo si es mi aliado

            strategy = self.code[self.code_state]

        elif self.code_state == len(self.code):
            # es mi aliado
            strategy = True

        return strategy

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    def process_results(self, my_strategy, other_strategy):
        if self.code_state == -1:
            pass

        elif self.code_state < len(self.code):
            # todavia estoy viendo si es mi aliado
            if other_strategy == self.code[self.code_state]:
                self.code_state = self.code_state + 1
            else:
                self.code_state = -1

        elif self.code_state == len(self.code):
            pass
