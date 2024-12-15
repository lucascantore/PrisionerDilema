from tournament.Tournament import Tournament
from precontract.players.GoodBoy_AllAlliance import GoodBoyWithAlliances
from precontract.players.GoodBoy_NoAlliance import GoodBoy


if __name__ == '__main__':
    competing_players_classes = [GoodBoyWithAlliances, GoodBoyWithAlliances, GoodBoyWithAlliances, GoodBoy]

    # competing_players_classes = [GoodBoy, GoodBoy, GoodBoy, GoodBoy]

    n_first_rounds = 10
    n_second_rounds = 5

    t = Tournament(competing_players_classes, n_first_rounds, n_second_rounds)

    t.play_tournament()
