from Prisoner import Prisoner

class PrisonerJuli(Prisoner):

    def __init__(self):
        self.TotalRounds = self.TotalOpponentCooperations = self.TotalSelfDeflections = self.OpponentLastStrategyCount = 0
        self.OpponentLastStrategy = True 
        self.name="PrisonerJuli"

    @staticmethod
    def name():
        return "PrisonerJuli"

    def pick_strategy(self):       
        if self.TotalRounds < 4:
            return True
             
        if self.OpponentLastStrategy == False and self.OpponentLastStrategyCount >= 2:
                return False
        
        if self.TotalOpponentCooperations/self.TotalRounds > 0.7:         
            if self.OpponentLastStrategy == True and self.OpponentLastStrategyCount >= 2 and self.TotalSelfDeflections/self.TotalRounds < 0.2:
                return False
            else:   
                return True
            
        return self.OpponentLastStrategy

    def process_results(self, my_strategy, other_strategy):
        self.TotalRounds += 1
        if my_strategy == False: 
            self.TotalSelfDeflections += 1

        if self.OpponentLastStrategy == other_strategy:
            self.OpponentLastStrategyCount += 1

        self.OpponentLastStrategy = other_strategy
        if other_strategy == True: 
            self.TotalOpponentCooperations += 1