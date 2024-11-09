from Prisoner import Prisoner
import random

class ElGrinch(Prisoner):

    def __init__(self):
        self.name = "El Grinch"
        self.tolerance = 0.5
        self.puntaje = self.otro_puntaje = 0
        self.diferencia = self.cant_empates = 20
        self.cant_partidas = 0
        self.cant_perdidas = 0
        self.coopero_antes = False

    def pick_strategy(self):

        if random.random() <= self.tolerance:
            return self.nunca_coopero()
        else:
            return self.que_sea_lo_que_random_quiere()
    
    def nunca_coopero(self):
        return False
    
    def que_sea_lo_que_random_quiere(self):
        return random.choice([True, False])

    def process_results(self, my_strategy, other_strategy):

        puntajes = self.score(my_strategy, other_strategy)

        self.cant_partidas += 1

        self.puntaje += puntajes[0]
        self.otro_puntaje += puntajes[1]

        self.coopero_antes = self.coopero_antes or other_strategy

        # Si más o menos estamos empatados
        if abs(self.puntaje - self.otro_puntaje) <= self.diferencia:

            self.cant_empates += 1
            
            if self.cant_empates >= 5 and self.coopero_antes:

                self.cant_empates = 0

                if self.tolerance > 0.5:
                    self.tolerance -= 0.1
                else:
                    self.tolerance += 0.1
        
        # Si pierde el grinch :(
        elif self.puntaje < self.otro_puntaje:

            self.cant_perdidas += 1

            if self.cant_perdidas == 5:

                if self.tolerance > 0.5:
                    self.tolerance = 0.2
                else:
                    self.tolerance = 0.8
            

    def score(self, strategy1, strategy2):
        if strategy1 and strategy2:
            return (1, 1)
        elif not strategy1 and strategy2:
            return (2, -1)
        elif strategy1 and not strategy2:
            return (-1, 2)
        else:
            return (0, 0)
