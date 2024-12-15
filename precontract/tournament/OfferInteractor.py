class OfferInteractor:

    def __init__(self, offer_queue, alliances, players):
        # array with offers.
        self.offer_queue = offer_queue

        # alliances map -> player number maps to its current alliance
        self.alliances = alliances


        self.players = players


    def propose_offer(self, receiver_player_index, sender_player_index, offer):
        alliance = self.alliances[sender_player_index]

        # we verify that we made a valid offer
        if not alliance.can_add_new_member_for(self.players[receiver_player_index], offer)\
                or len(self.alliances[receiver_player_index].members)>1:
            return False


        self.offer_queue[receiver_player_index].append(offer)
        return True

    # return True if the offer was successfully accepted
    # return False if offer could not be accepted.
    def accept_offer(self, offer, accepted_player):
        alliance = self.alliances[offer.alliance_index()]

        # we verify that we can accept the offer for the given alliance
        if not alliance.can_add_new_member_for(accepted_player,offer)\
                or len(self.alliances[accepted_player.number].members)>1:
            return False


        # we invalidate new member old alliance -> since they can only have 1 alliance at a time
        self.alliances[accepted_player.number].invalidate_alliance()

        # we add the new member to the alliance
        alliance.add_member(accepted_player, offer)
        # modify new members alliance
        self.alliances[accepted_player.number] = alliance

        return True
