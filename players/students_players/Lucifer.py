from Prisoner import Prisoner

"""
Lucifer: a Prisoner who always defects.
"""


class Lucifer(Prisoner):
    def __init__(self):
        self.name = "Lucifer"

    @staticmethod
    def name():
        return "Lucifer"

    def pick_strategy(self):
        return False
