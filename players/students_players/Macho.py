from Prisoner import Prisoner
import random

class Macho(Prisoner):

    def __init__(self):
        self.total_rounds = self.total_coop = self.btb_coop = 0
        self.total_coop_op = 0
        self.last_strategy_op = True
        self.betrayals = 0
        self.mode = "friendly"
        self.name="Macho"

    @staticmethod
    def name():
        return "Macho"

    """
    total_rounds : nro. total de rondas hasta ahora
    total_coop : cantidad de veces que cooperé
    btb_coop : nro. de veces seguidas que cooperé
    total_coop_op : nro. total de veces que el (mismo) oponente cooperó
    """

    def pick_strategy(self):
        if self.mode == "friendly": # Si estoy en modo amistoso
            if self.last_strategy_op == True: # si el oponente la última vez cooperó
                return True # coopero
            else: # en caso contrario
                r = random.randint(0, 9) 
                if r >= 7: # El 30% de las veces coopero
                    return True
        elif self.mode == "neutral": # Si estoy en modo neutral
            if self.last_strategy_op == True: # si el oponente la última vez cooperó
                r = random.randint(0, 9)
                if r >= 2: # El 80% de las veces coopero
                    return True
        return False # Si estoy en modo hostil o no cooperé en los casos anteriores, disiento

    def process_results(self, my_strategy, other_strategy):
        self.total_rounds += 1
        if self.total_rounds == 20: # Cada 20 rondas cambio de modo y reseteo los contadores
            if self.betrayals > 5: # Si me traicionó más de 5 veces, cambio a modo hostil
                self.mode = "hostile"
            elif self.betrayals > 0: # Si me traicionó al menos una vez, cambio a modo neutral
                self.mode = "neutral"
            else: # Si no me traicionó nunca, cambio a modo amistoso
                self.mode = "friendly"

            # Reseteo los contadores
            self.betrayals = 0
            self.total_rounds = 0
            self.total_coop = 0
            self.total_coop_op = 0
            self.btb_coop = 0

        if my_strategy == True: # Si la última vez cooperé
            self.total_coop += 1 # Incremento la cantidad total de veces que cooperé
            self.btb_coop += 1 # y la cantidad de veces seguidas que cooperé
            if self.last_strategy_op == False: # Si el oponente la última vez no cooperó
                self.betrayals += 1 # Incremento la cantidad de veces que me traicionó

        elif my_strategy == False: # en caso contrario
            self.btb_coop = 0 # pongo en 0 la cantidad de veces seguidas que cooperé

        self.last_strategy_op = other_strategy # actualizo la última estrategia del oponente con la actual
        if other_strategy == True: # si el oponente la última vez cooperó
            self.total_coop_op += 1 # incremento la cantidad total de veces que cooperó
