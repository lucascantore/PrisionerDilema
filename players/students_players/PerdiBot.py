from Prisoner import Prisoner

"""
PerdiBot: el bot que te hace perder

"""


class PerdiBot(Prisoner):
    def __init__(self):
        self.name = "PerdiBot"

        self.precedentes_coop = {True: 0, False: 0}
        self.prev_strategy = None

    @staticmethod
    def name():
        return "PerdiBot"

    def pick_strategy(self):
        return (
            # nunca me traicionaron
                self.precedentes_coop[False] == 0 or
                # acepto que me traicionen una vez por cada 10
                self.precedentes_coop[True] >= 10 * self.precedentes_coop[False]
        )

    def process_results(self, my_strategy, other_strategy):
        # si jugué cooperar
        if self.prev_strategy == True:
            # me guardo lo que jugó el otro
            self.precedentes_coop[other_strategy] += 1

        self.prev_strategy = my_strategy
