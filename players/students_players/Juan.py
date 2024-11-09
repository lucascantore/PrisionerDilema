
from Prisoner import Prisoner
import random

class Juan(Prisoner):
    def __init__(self):
        # General statistics 
        self.N = 0
        self.other_C = 0
        # Scouting attributes
        self.scoutingPhase = 75
        self.otherChoiceOnScouting = []
        self.myChoiceOnScouting = []
        self.didScouted = False
        # Consider copy cat after scouting phase
        self.goForCopyCatApproach = False
        self.lastOpponentChoice = False
        # Analyzing coincidences to force next strategy
        self.myLast5 = [None] * 5
        self.otherLast5 = [None] * 5
        self.lastCheckpointVerification = 0
        self.name="Juan"

    @staticmethod
    def name():
        return "Juan"

    def pick_strategy(self):
        randPick = random.random()
        # Scouting phase, cooperate much more to see how the opponent behaves
        if self.N <= self.scoutingPhase:
            return randPick > 0.25
        
        # If opponent is not collaborating too much, then don't confess for now
        if self.other_C / self.N <= 0.1:
            return False

        # On the other hand, if agreement was found to confess, then copy the last opponent's choice
        if self.goForCopyCatApproach:
            return self.lastOpponentChoice

        # If still not clear, just go with the statistics approach (considering opponent's confession)
        other_C_probability = self.other_C / self.N
        if (randPick > other_C_probability):
            return False
        else:
            return True

    def process_results(self, my_strategy, other_strategy):
        self.lastOpponentChoice = other_strategy
        if self.N <= self.scoutingPhase:
            self.myChoiceOnScouting.append(my_strategy)
            self.otherChoiceOnScouting.append(other_strategy)
        elif not self.didScouted:
            self.analyzeScouting()
            self.didScouted = True
        else:
            self.myLast5[self.lastCheckpointVerification] = my_strategy
            self.otherLast5[self.lastCheckpointVerification] = other_strategy
            
            if (self.lastCheckpointVerification == 4):
                # Check if copyCatApproach is worth it
                C_coincidences = 0
                C_loss = 0
                for i in range(len(self.myLast5)):
                    if self.myLast5[i] == self.otherLast5[i] and self.myLast5[i] == True:
                        C_coincidences += 1
                    elif self.myLast5[i] != self.otherLast5[i] and self.myLast5[i] == True:
                        C_loss += 1
                # If we have coincidences but also not much loss coming from (C, D) variaton, then choose copyCat
                if (C_coincidences > 1 and C_loss <= 2):
                    self.goForCopyCatApproach = True
                    self.lastOpponentChoice = other_strategy
                else:
                    self.goForCopyCatApproach = False
                # Reset checkpoint
                self.lastCheckpointVerification = 0
            else:
                self.lastCheckpointVerification += 1
        # Update stats
        self.N += 1
        if other_strategy:
            self.other_C += 1
    
    def analyzeScouting(self):
        C_coincidences = 0
        C_otherCount = 0
        for i in range(len(self.myChoiceOnScouting)):
            C_coincidences += self.myChoiceOnScouting[i] == True and self.otherChoiceOnScouting[i] == self.myChoiceOnScouting[i]
            C_otherCount += self.otherChoiceOnScouting[i]
        # Start with copy cat if confession coincidences were good enough (or pretty frequent)
        if (C_coincidences >= 0.3 or C_otherCount / self.N >= 0.5):
            self.goForCopyCatApproach = True
