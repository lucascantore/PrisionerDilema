from precontract.players.Player import Player
from precontract.tournament.Offer import Offer


class GoodBoyWithAlliances(Player):
    def __init__(self, my_number):
        super().__init__(my_number)

    def pick_strategy(self):
        return True

    def process_results(self, strategy, opponent_strategy):
        pass

    # contract_interactor is used to propose offers to other players
    # personal_contract_queue has the offers proposed to the player
    def process_contracts(self, offer_interactor, personal_offer_queue):
        # Accepts all alliances that it can accept
        for o in personal_offer_queue:
            success = offer_interactor.accept_offer(o, self)
            # print("success in accepting: ", success)

        my_alliance = offer_interactor.alliances[self.number]

        # while we still can at least offer 0.1, then we will offer it to other players
        for p in offer_interactor.players:
            if my_alliance.remaining_receive_percentage() > 0.1:
                offer = Offer(0.1, 0.1,my_alliance)
                success = offer_interactor.propose_offer(p.number, self.number, offer)
                # print("success in offering: ", success)



