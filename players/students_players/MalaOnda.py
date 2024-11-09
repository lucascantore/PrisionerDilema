from Prisoner import Prisoner

"""
MalaOnda es un prisionero que generalmente disiente (y por eso mala onda).
Además, intenta de tender trampas para aquellos oponentes que intenten cooperar.
Cada tanto coopera algunas veces seguidas y después vuelve a disentir.

"""


class MalaOnda(Prisoner):
    def __init__(self):
        self.name = "Mala Onda"  # nombre completo a imprimir

        self.my_last = False
        self.my_consecutive_defects = 0
        self.my_consecutive_cooperations = 0

        self.other_last = False  # Asumo que no coopera

        # Configuraciones
        self.max_consecutive_defects = 25
        self.cooperation_tolerance = 3

    @staticmethod
    def name():
        return "Mala Onda"

    def pick_strategy(self):
        # Si lo último que hice fue cooperar,
        if self.my_last:
            if self.other_last:
                # Si el otro ya cooperó, ya cayó en la trampa, volvemos a
                # disentir
                return False

            # Sino, intento seguir cooperando hasta la tolerancia
            if self.my_consecutive_cooperations >= self.cooperation_tolerance:
                return True

        else:
            # Cada tanto empiezo a cooperar un poco
            if self.my_consecutive_defects >= self.max_consecutive_defects:
                return True

            return False

    def process_results(self, my_strategy, other_strategy):
        self.my_last = my_strategy
        self.other_last = other_strategy

        if not my_strategy:
            self.my_consecutive_defects += 1
            self.my_consecutive_cooperations = 0
        else:
            self.my_consecutive_defects = 0
            self.my_consecutive_cooperations += 1
