from Prisoner import Prisoner

class JohnTravolta(Prisoner):
      
    def __init__(self):
        self.ultima_jugada = None 
        self.jugada_favorable = None
        self.name="John Travolta"

    @staticmethod
    def name():
        return "John Travolta"

    def pick_strategy(self):
 
        if self.ultima_jugada is None:
            return True
        else:
            if self.jugada_favorable == True:
                return self.ultima_jugada
            else:
                return not self.ultima_jugada
            
    def process_results(self, my_strategy, other_strategy):
         
        self.ultima_jugada = my_strategy

        if my_strategy == other_strategy:
            self.jugada_favorable = True
        else:
            self.jugada_favorable = False



