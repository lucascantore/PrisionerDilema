from Prisoner import Prisoner


class War(Prisoner):

    def __init__(self):
        self.other_strategy = True  # asumo que el oponente arranca cooperando
        self.name = "War"  # nombre completo a imprimir

    @staticmethod
    def name():
        return "War"

    def pick_strategy(self):
        return self.other_strategy  # La idea es intentar maximizar mi cooperacion siempre y cuando el oponente este dispuesto

    # Si yo confieso y el disiente, yo voy a disentir hasta q el oponente confiese llevando a total de 1 esa subsecuencia, el peor de los casos es enfrentarme a alguien q disienta siempre llevandome a un total de -1
    # Asumo q mis oponentes buscaran Maximizar sus puntos por lo que la probabilidad de enfrentarme a alguien asi es baja
    # Solo perderia puntos respecto a mi oponente si el disiente en un determinado momento y nunca mas confiesa, pero la perdida es minima
    # En el mejor caso, me enfrento a alguien q siempre confiesa y ambos sacaremos un puntaje muy valioso

    def process_results(self, my_strategy, other_strategy):
        self.other_strategy = other_strategy
