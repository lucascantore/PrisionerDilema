from Prisoner import Prisoner


class AlCapone(Prisoner):

    def __init__(self):
        self.N = 0
        self.Oh = []
        self.Eh = []
        self.name = "Al Capone"

    @staticmethod
    def name():
        return "Al Capone"

    """
    N : Rounds number
    Oh : Own history (1 for cooperate, 0 opposite case)
    Eh : Enemy history (1 for cooperate, 0 opposite case)
    """

    def pick_strategy(self):

        res1 = obtain_cooperations_number(self.Oh)
        res2 = obtain_cooperations_number(self.Eh)
        if res1 > res2:  # if the enemy cooperates less
            return False
        else:
            return True

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy:
            self.Oh.append(1)
        elif not my_strategy:
            self.Oh.append(0)
        if other_strategy:
            self.Eh.append(1)
        elif not other_strategy:
            self.Eh.append(0)


def obtain_cooperations_number(history):
    res = 0
    for e in history:
        res += e
    return res
