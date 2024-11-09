from Prisoner import Prisoner
import random

"""
La estrategia consiste en calcular la proporción de
las veces que el oponente disiente. Si la proporción
es demasiado alta (en base a un valor elgido arbitrariamente)
siempre va a disentir. Mientras mas haya cooperado el oponente
más cooperará.
"""

class Lucifer735(Prisoner):
    def __init__(self):
        super().__init__()
        #inicio valores del prisionero en 0
        self.rounds = self.c_total = self.d_total = 0
        #inicio la cantidad de veces que el oponente disintió
        self.opp_d_total = 0
        self.c = 0
        self.d_prob = 0.5 #igual posibilidad de cooperar o no hacerlo
        #inicio el valor elegido como proporción alta
        self.d_prop_alta = 0.3
        self.name = "Lucifer735"

    @staticmethod
    def name():
        return "Lucifer735"

    #calcula la proporción de veces que el oponente disintió
    def get_opp_d_prop(self):
        return self.opp_d_total/max(self.rounds,1)

    def pick_strategy(self):
        #en la primera ronda siempre disiente
        if self.rounds == 0:return False
        #si el oponente disientió demasiado, disiento
        if self.get_opp_d_prop() > self.d_prop_alta:
            return False
        #si coopero demasiado, disiento
        if self.c > 3 and self.c_total/self.rounds > 0.5:
            return False
        return (random.randint(0,9)/10) > self.d_prob

    def process_results(self, my_strategy, other_strategy):
        self.rounds += 1
        #actualizo valores
        if not other_strategy:
            self.opp_d_total +=1
        if my_strategy:
            self.c += 1
            self.c_total += 1
        else:
            self.d_total += 1
            self.c = 0
        #si el oponente coopera mucho, aumento la probabilidad de cooperar
        if (self.d_prob > self.get_opp_d_prop() and 
            self.d_prob > self.d_prop_alta):
            self.d_prob -= 0.1
        #si el oponente disiente mcucho, aumento la probabilidad de disentir
        if self.opp_d_total > self.d_total:
            self.d_prob += 0.1
        
