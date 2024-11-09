from Prisoner import Prisoner

"""
Jesus: a Prisoner who always cooperates
"""
class Jesus(Prisoner):

    def __init__(self):
        self.name = "Jesus"  # nombre completo a imprimir

    @staticmethod
    def name():
        return "Jesus"
    
    def pick_strategy(self):
        return True
