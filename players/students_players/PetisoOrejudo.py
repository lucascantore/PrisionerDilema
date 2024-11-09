

from Prisoner import Prisoner




class PetisoOrejudo(Prisoner):


    def __init__(self):
        self.N = self.C = self.ci = 0 
        self.eC = 0
        self.other_strategy = True 
        self.name="PetisoOrejudo"

    @staticmethod
    def name():
        return "PetisoOrejudo"

    """
    N : nro. total de rondas hasta ahora
    C : cantidad de veces que cooperé
    ci : nro. total de veces seguidas que cooperé
    eC : nro. total de veces que el (mismo) oponente cooperó
    """

#Esta función determina la estrategia a usar en cada ronda, pudiendo mirar cualquier
#atributo propio del objeto definido como jugador, en este caso ElGuason.

    def pick_strategy(self):
 
        return False
#Solamente dicentir siempre puede parecer muy simple, pero esta estrategia la baso en el que (D,D) es el equilibro de Nash.
#Como ese es el equilibro, se esperaria que una vez lleguen ahi, ningun aegnte cambiara su decision.
#Siempre dicentir busca garantizar que el otro jugador no consiga mas puntos que yo, como minimo terminamos con lo mismo, como mejor caso coopera al principio.
#Como el objetivo del torneo es que nadie consiga mas puntos que uno y no necesariamente maximizar la ganancia, creo que esta es la mejor opcion.



