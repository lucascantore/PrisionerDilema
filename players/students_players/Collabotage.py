from Prisoner import Prisoner

class Collabotage(Prisoner):

    # desarrollado contra el guason

    def __init__(self):
        self.name="Collabotage"
        self.collab_probability = 0.55      #criterio: si espera colaboracion (empieza suponiendo 0.55)
        
        self.collab_threshold = 0.5         #constante que determina cuando se coopera
        self.sabotage_threshold = 0.6       #constante que determina cuando se traiciona

        self.rounds = 0
        self.opponent_collabs = 0
        self.points = 0

    @staticmethod
    def name():
        return "Collabotage"
        
    def pick_strategy(self):
        if self.collab_probability >= self.sabotage_threshold:
            return False
        elif self.collab_probability >= self.collab_threshold:
            return True
        else:
            return False
    def process_results(self, my_strategy, other_strategy):
        self.rounds += 1
        self.opponent_collabs += other_strategy
        
        if my_strategy and other_strategy:
            self.points += 1
        elif my_strategy and not other_strategy:
            self.points += -2
        elif not my_strategy and other_strategy:
            self.points += 1
        
        self.collab_probability = self.opponent_collabs / self.rounds
