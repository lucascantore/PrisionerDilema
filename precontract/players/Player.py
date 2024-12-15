class Player:
    def __init__(self, my_number):
        self.number = my_number

    def pick_strategy(self):
        pass

    def process_results(self, strategy, opponent_strategy):
        pass

    # contract_interactor is used to propose offers to other players
    # personal_contract_queue has the offers proposed to the player
    def process_contracts(self, offer_interactor, personal_offer_queue):
        pass
