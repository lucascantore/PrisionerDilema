import copy


class Offer:

    def __init__(self, give, receive, alliance):
        # if creating an invalid alliance, then raise error
        if give < 0 or give > 1 or receive < 0 or receive > 1:
            raise ValueError("Give and receive must be between 0 and 1")

        # percentage that will be given to the alliance
        self.give = give # we assume good faith that players won't modify give
        # percentage that will be received from the alliance total gains
        self.receive = receive # we assume good faith that players won't modify receive
        # the alliance that the player will join if offer is accepted
        self.alliance = alliance # we assume good faith that players won't modify the alliance

    def alliance_index(self):
        return self.alliance.alliance_index()
