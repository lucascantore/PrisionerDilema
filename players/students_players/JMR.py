# Mi estrategia es "tit for tat con perdón" con algunas variantes
# (luego de 183 de disentir se coopera y cada ronda tiene una probabilidad del 5% se hace lo opuesto a lo esperado) 

from Prisoner import Prisoner
import random


class JMR(Prisoner):
    def __init__(self):
        self.D = 0  # cantidad de rondas seguidas que el oponente disiente
        self.other_strategy = True  # asumo (arbitrariamente) que el oponente arranca cooperando
        self.name = "JMR"  # nombre

    @staticmethod
    def name():
        return "JMR"

    def pick_strategy(self):

        if self.other_strategy == True or self.D == 1 or self.D == 183:  # si el oponente coopera o disintió exactamente 1 o 183 veces
            return True  # coopero
        else:
            return False  # disiento

    def process_results(self, my_strategy, other_strategy):
        self.other_strategy = other_strategy  # actualizo la última respuesta del oponente

        if other_strategy == False:
            self.D += 1  # si el oponente disiente sumo 1 a la cantidad de veces seguidas que disintió
        else:
            self.D = 0  # si el oponente coopera pongo en 0 la cantidad de veces seguidas que disintió

        if random.random() < 0.05:  # con una probabilidad del 5% invierto la estrategia esperada
            return not self.pick_strategy()
        else:
            return self.pick_strategy()
