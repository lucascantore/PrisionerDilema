from precontract.players.Player import Player

class GoodBoy(Player):
    def __init__(self, my_number):
        super().__init__(my_number)

    def pick_strategy(self):
        return True

    def process_results(self, strategy, opponent_strategy):
        pass

    # contract_interactor is used to propose offers to other players
    # personal_contract_queue has the offers proposed to the player
    def process_contracts(self, offer_interactor, personal_offer_queue):
        pass