from Prisoner import Prisoner


class LosConfundidores(Prisoner):

    def __init__(self):
        self.N = 0
        self.count_consecutive_enemy_betrays = 0
        self.enemy_betrays_2_times_in_a_row = False
        self.other_strategy = True
        self.name = "LosConfundidores"

    @staticmethod
    def name():
        return "LosConfundidores"

    def pick_strategy(self):
        if self.N == 0: return True
        if self.enemy_betrays_2_times_in_a_row: return False
        return self.other_strategy

    def process_results(self, _, other_strategy):
        self.N += 1
        self.other_strategy = other_strategy
        if other_strategy == True:
            self.count_consecutive_enemy_betrays = 0

        else:
            self.count_consecutive_enemy_betrays += 1
            if self.count_consecutive_enemy_betrays >= 2:
                self.enemy_betrays_2_times_in_a_row = True
