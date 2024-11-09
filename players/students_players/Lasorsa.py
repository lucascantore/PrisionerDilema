from Prisoner import Prisoner
from random import random

class Lasorsa(Prisoner):

    def __init__(self):
        self.N = 11
        self.a = 1
        self.b = 1
        self.ps = [0] * self.N
        for i in range(self.N):
            p = i/(self.N+1)
            self.ps[i] = p**self.a * (1-p)**self.b
        suma = sum(self.ps)
        for i in range(self.N):
            self.ps[i] /= suma
        self.name = "Lasorsa"

    @staticmethod
    def name():
        return "Lasorsa"
    
    def pick_strategy(self):
        prob = 0
        for i in range(self.N):
            prob += self.ps[i] * i/(self.N-1)
        return random() < prob

    def process_results(self, my_strategy, other_strategy):
        for i in range(self.N):
            if other_strategy:
                self.ps[i] = i/(self.N-1) * self.ps[i]
            else:
                self.ps[i] = (1-i/(self.N-1)) * self.ps[i]
        suma = sum(self.ps)
        for i in range(self.N):
            self.ps[i] /= suma
               
