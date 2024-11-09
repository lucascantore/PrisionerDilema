

from Prisoner import Prisoner
import random


class Nashville(Prisoner):


    def __init__(self):
        self.N = 0                         # inicializo los totales
        self.oponente = []                  # Movimientos del oponente
        self.proximo_movimiento = True     # Movimiento inicial
        self.other_strategy = True         # asumo (arbitrariamente) que el oponente arranca cooperando
        self.ultimas_dos = []              # ultimos 2 moviminetos del oponente
        self.name = "Nashville"              # nombre completo a imprimir

    @staticmethod
    def name():
        return "Nashville"

    """
    N : nro. total de rondas hasta ahora
    oponente : lista de acciones del oponente
    ultimas_dos: ultimas dos jugadas del oponente
    
    """



    def pick_strategy(self):
         
         
        if self.N != 0:
            if(len(self.ultimas_dos)!= 0 and sum(self.ultimas_dos)==0):
                   # caso oponente no coopero ultimamente
                   self.proximo_movimiento = False
                   
                   
            elif((sum(self.oponente)/self.N)>0.3 and (sum(self.oponente)/self.N)<=0.6 ):
                   # (P(cooperar) = 0,03125)
                   self.proximo_movimiento = random.randint(0,1) * random.randint(0,1) * random.randint(0,1) * random.randint(0,1) * random.randint(0,1)
    
                   

        return self.proximo_movimiento
        
 


    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        self.other_strategy = other_strategy
        self.oponente.append(other_strategy)
        self.ultimas_dos.append(other_strategy)
        if self.N %3 == 0:
           self.ultimas_dos = []





