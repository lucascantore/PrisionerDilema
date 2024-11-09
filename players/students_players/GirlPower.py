from Prisoner import Prisoner


class GirlPower(Prisoner):

    def __init__(self):
        self.N = 0 
        self.C = 0
        self.NC= 0
        self.strategy = True #empiezo cooperando
        self.name="Girl Power" #nombre completo a imprimir

    @staticmethod
    def name():
        return "Girl Power"

    """
    N : nro. total de rondas hasta ahora
    C : cantidad de veces que cooperó mi oponente
    NC : cantidad de veces que no cooperó mi oponente
    strategy: mi estrategia
    """

    def pick_strategy(self):
        return self.strategy #mi estrategia depende de lo que vaya haciendo mi oponente,trato de copiar lo que elige en promedio


    def process_results(self, my_strategy, other_strategy): 
        self.N += 1
        if other_strategy:
            self.C += 1 #si coopera
        else:
            self.NC += 1
        coopera = self.C/self.N #calculo el promedio de las veces que coopera
        no_coopera = self.NC/self.N #calculo el promedio de las veces que no coopera
        if coopera > no_coopera: #copio la estrategia según lo que más hace en promedio
            self.strategy = True
        else:
            self.strategy = False  


