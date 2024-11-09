from Prisoner import Prisoner
import random


class RobinHood(Prisoner):

    def __init__(self):
        self.N = self.C = self.ci = 0  # inicializo los totales
        self.eC = 0  # Cuántas veces cooperó el otro en total
        self.eCi = 0  # cuántas veces seguidas cooperó el otro
        self.other_strategy = True  # asumo (arbitrariamente) que el oponente arranca cooperando
        self.name = "RobinHood"  # nombre completo a imprimir

    @staticmethod
    def name():
        return "RobinHood"

    """
    N : nro. total de rondas hasta ahora
    C : cantidad de veces que cooperé
    ci : nro. total de veces seguidas que cooperé
    eC : nro. total de veces que el (mismo) oponente cooperó
    
    Estrategia general:
1) Elegimos bajar la tolerancia de las veces consecutivas que vamos a cooperar.
2) si cooperé la jugada anterior, y además: cooperé más del 30% de las veces en lo que va del total o el rival no cooperó                               ni tres veces del total, entonces dejo de cooperar. Porque si sigo cooperando y el otro no está cooperando, es lo peor que me puede pasar porque pierdo puntos, y quiero maximizar mi ganancia.
3) en el caso contrario, hay una probabilidad de 0,5 de que coopere en la próxima jugada, y en su defecto hago lo mismo que hizo           mi rival en la jugada anterior.   
        
        
    """

    def pick_strategy(self):
        if self.ci > 1:  # Si cooperé muchas veces seguidas
            if self.C / self.N > 0.3 or self.eCi < 3:  # Y cooperé muchas veces en total o el otro no cooperó varias veces seguidas
                return False  # disiente
            else:
                return True  # coopera
        else:
            r = random.randint(0, 9)  # Genera un número aleatorio de 0 a 9
            if r < 5:  # Esta proporción de veces
                return self.other_strategy  # hago la última estrategia del oponente
            else:
                return True  # coopero

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    # En este ejemplo, el prisionero sólo recordará la última estrategia del oponente. Si necesitan recordar más,
    # pueden hacerlo, incluso armar el historial (en una lista, tupla, diccionario, etc.)

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if my_strategy == True:  # si la última vez cooperé, decido cooperar
            self.C += 1  # incremento la cantidad total de veces que cooperé
            self.ci += 1  # y la cantidad de veces seguidas que cooperé

        elif my_strategy == False:  # en caso contrario
            self.ci = 0  # pongo en 0 la cantidad de veces seguidas que cooperé

        self.other_strategy = other_strategy  # actualizo la última estrategia del oponente con la actual
        if other_strategy == True:  # si el oponente la última vez cooperó
            self.eC += 1  # incremento la cantidad total de veces que cooperó
            self.eCi += 1
        else:
            self.eCi = 0
