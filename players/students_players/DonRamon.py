from Prisoner import Prisoner
import random

class DonRamon(Prisoner):

    def __init__(self):
        self.N_since_last_forgiveness = self.other_defect = self.other_coop = 0
        self.retaliation_count = 0
        self.name="Don Ramon" # La venganza nunca es buena

    @staticmethod
    def name():
        return "Don Ramon"

    def pick_strategy(self):
        retaliation_chance = 0
        if (self.N_since_last_forgiveness != 0):
            # Mientras mas me hayan traicionado, mas alta sera la chance de venganza
            retaliation_chance = self.other_defect / self.N_since_last_forgiveness

        forgiveness_chance = 0
        if (self.N_since_last_forgiveness != 0 and self.retaliation_count > 0):
            # La cantidad de venganzas aporta a la chance de perdonar relativamente respecto al historial de traicion
            retaliation_factor = 0
            if (self.other_defect != 0):
                retaliation_factor = self.retaliation_count / self.other_defect

            forgiveness_chance = (self.other_coop + retaliation_factor) / self.N_since_last_forgiveness

        if random.random() <= retaliation_chance:
            # Un poco de venganza, pero cada venganza suma un poco de chance de perdonar
            self.retaliation_count += 1
            return False

        if random.random() <= forgiveness_chance:
            # Perdono la historia, borron y cuenta nueva
            self.N_since_last_forgiveness = 0
            self.other_defect = 0
            self.other_coop = 0
            self.retaliation_count = 0

        # Por defecto trato de cooperar
        return True

    def process_results(self, my_strategy, other_strategy):
        self.N_since_last_forgiveness += 1
        if (other_strategy):
            self.other_coop += 1
        else:
            self.other_defect += 1
