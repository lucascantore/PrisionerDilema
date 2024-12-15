from itertools import combinations
from random import shuffle

from precontract.tournament.OfferInteractor import OfferInteractor
from precontract.tournament.Alliance import Alliance


def prisioner_dilema_score(strategy1, strategy2):
    if strategy1 and strategy2:
        return 1, 1
    elif not strategy1 and strategy2:
        return 2, -1
    elif strategy1 and not strategy2:
        return -1, 2
    else:
        return 0, 0


class Tournament():

    # competing_players = list of players class that will compete in the tournament
    # n_first_rounds = rounds of the pre-game, where players make contracts
    # n_second_rounds = rounds of the game, where players actually play the game
    def __init__(self, competing_players_classes, n_first_rounds=20, n_second_rounds=20):
        self.competing_players_classes = competing_players_classes
        self.n_first_rounds = n_first_rounds
        self.n_second_rounds = n_second_rounds

    def score(self, strategy1, strategy2):
        # we can switch the score function
        return prisioner_dilema_score(strategy1, strategy2)

    def play_match_second_part(self, player1, player2):
        score1 = 0
        score2 = 0
        for _ in range(self.n_second_rounds):
            strategy1 = player1.pick_strategy()
            strategy2 = player2.pick_strategy()
            s1, s2 = self.score(strategy1, strategy2)
            score1 += s1
            score2 += s2
            player1.process_results(strategy1, strategy2)
            player2.process_results(strategy2, strategy1)
        return score1, score2

    def play_tournament(self):
        # initialize players array
        players = []
        # a map that given a player number returns an array with offers offered to the player
        offer_queue = {}
        # a map that given a player number, returns the alliance that they are a part of
        alliances = {}

        player_number = 0
        for player_class in self.competing_players_classes:
            # each player is assigned a distinct number
            players.append(player_class(player_number))
            player_number +=1

        # the player number is used to map the player alliance and its offer queue
        for p in players:
            offer_queue[p.number] = []
            alliances[p.number] = Alliance(p)

        # first part of the tournament
        # Iterate n_first_rounds times over the whole list of players
        # so they can make contracts
        for _ in range(self.n_first_rounds):
            for i in range(len(players)):
                players[i].process_contracts(
                    OfferInteractor(offer_queue, alliances, players),
                    offer_queue[i]
                )

        for a in alliances:
            print(f"Alliance N{a}: ", alliances[a])


        ########   second part of the tournament   ########

        # scores for every player
        scores = len(players)*[0]
        # scores accumulated by alliance
        alliance_accumulated_score = len(alliances)*[0]

        matches = list(combinations(range(len(players)), 2))
        shuffle(matches)

        print("matches: ", matches)

        # Play all matches
        for match in matches:
            (score1, score2) = self.play_match_second_part(
                players[match[0]],
                players[match[1]]
            )
            actual_player_score1, alliance_score1 = self.get_player_and_alliance_accumulated_scores(match[0],score1, alliances)
            scores[match[0]] +=actual_player_score1
            alliance_accumulated_score[alliances[match[0]].alliance_index()] +=alliance_score1

            actual_player_score2, alliance_score2 = self.get_player_and_alliance_accumulated_scores(match[1],score2, alliances)
            scores[match[1]] += actual_player_score2
            alliance_accumulated_score[alliances[match[1]].alliance_index()] +=alliance_score2


        # redistribuir los puntos acumulados en cada alianza.
        # reallocate alliance acumulated points
        for p in players:
            scores[p.number] += alliance_accumulated_score[alliances[p.number].alliance_index()] * alliances[p.number].get_received_percentage_for(p.number)


        # return the scores
        print("scores: ", scores)
        return scores

    # returns tuple with what the players earns for himself and what he earns for the alliance
    def get_player_and_alliance_accumulated_scores(self, player_index, player_score, alliances):
        score_given_to_alliance = alliances[player_index].members_give[player_index] * player_score
        return player_score - score_given_to_alliance, score_given_to_alliance