from Prisoner import Prisoner


class TeammateTipForTatPointReceiver(Prisoner):

    def __init__(self):
        self.name = "TeammateTipForTatPointReceiver"  # nombre completo a imprimir
        self.code = [
            True, True, True, False, False, False, False, True, False, False,
            # False, False, False, False, True, False, False, False, False, True
        ]
        self.code_state = 0
        self.next_strategy = True

    # Esta función determina la estrategia a usar en cada ronda

    def pick_strategy(self):
        strategy = False

        if self.code_state == -1:
            return self.next_strategy

        elif self.code_state < len(self.code):
            # todavia estoy viendo si es mi aliado

            strategy = self.code[self.code_state]

        elif self.code_state == len(self.code):
            # es mi aliado
            strategy = False

        return strategy

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    def process_results(self, my_strategy, other_strategy):
        if self.code_state == -1:
            self.next_strategy = other_strategy

        elif self.code_state < len(self.code):
            # todavia estoy viendo si es mi aliado
            if other_strategy == self.code[self.code_state]:
                self.code_state = self.code_state + 1
            else:
                self.code_state = -1

        elif self.code_state == len(self.code):
            pass
