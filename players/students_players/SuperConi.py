from Prisoner import Prisoner


class SuperConi(Prisoner):

    def __init__(self):
        self.name = "SuperConi"

        # current state
        self.state = "C"
        # number of rounds played
        self.round = 0
        # number of times the opponent defected
        self.oppDefection = 0

        # number of times the opponent defected while in state D
        self.defectCycle = 0
        # every how many defecting rounds it will try to forgive
        self.defectCycleLimit = 10
        # if it already forgave once
        self.forgave = False

    @staticmethod
    def name():
        return "SuperConi"

    def pick_strategy(self):
        # C: cooperate
        if self.state == "C":
            return True

        # D: defect
        if self.state == "D":
            return False

        # N: neutral - will do what the oponent does
        if self.state == "N":
            return False

        # F: forgive - will cooperate even if they've been defecting
        if self.state == "F":
            return True

    def process_results(self, myStrategy, oppStrategy):
        self.round += 1

        if oppStrategy == False:
            self.oppDefection += 1

        if self.state == "C":
            if oppStrategy == False:
                self.state = "D"
            return

        if self.state == "D":
            if oppStrategy == True:
                self.state = "N"
            else:
                self.defectCycle += 1
                if self.defectCycle >= self.defectCycleLimit:
                    # it's been too many rounds defecting, let's try to cooperate
                    if not (self.forgave and self.oppDefection >= self.round * 0.95):
                        # if it never forgave, it will do it
                        # if it already forgave, the opponent doesn't have to have defected more than 95% of times
                        self.forgave = True
                        self.defectCycle = 0
                        self.state = "F"
            return

        if self.state == "N":
            if oppStrategy == True:
                self.state = "C"
            else:
                self.state = "D"
            return

        if self.state == "F":
            if oppStrategy == True:
                self.state = "N"
            else:
                self.state = "D"
            return
