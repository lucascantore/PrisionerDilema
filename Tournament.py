from itertools import combinations
from random import shuffle

from players import ElGuason
from players import GreedyWizard

"""
Prisoners' dilemma tournament
"""


class Tournament:
    """
  Initialize the tournament

  Parameters
  ----------
  competing: list of competing Prisoner subclasses
  n_rounds: rounds per match
  """

    def __init__(self, competing, n_rounds):
        self.competing = competing
        self.scores = len(competing) * [0]
        self.n_rounds = n_rounds

    """
  Score a single round

  Parameters
  ----------
  strategy1: bool
    First Prisoner's strategy

  strategy2: bool
    Second Prisoner's strategy

  Returns
  -------
  (score1, score2): (int, int)
    (1,1) if both cooperate,
    (0,0) if both defect, and
    (2,0) or (0,2) if one cooperates and one defects
  """

    def score(self, strategy1, strategy2):

        if strategy1 and strategy2:
            return (1, 1)
        elif not strategy1 and strategy2:
            return (2, -1)
        elif strategy1 and not strategy2:
            return (-1, 2)
        else:
            return (0, 0)

    """
  Play a single match

  Parameters
  ----------
  prisoner1: subclass of Prisoner
    First prisoner competing in the match

  prisoner2: subclass of Prisoner
    Second prisoner competing in the match

  n_rounds: int, optional
    Number of rounds in the match. If no value is
    provided, the number of rounds defaults to
    the default value for the tournament.

  Returns
  -------
  (int, int): scores for prisoner1 and prisoner2
  """

    def play_match(self, prisoner1, prisoner2, n_rounds=None):

        # Create instances of each prisoner
        p1 = prisoner1()
        p2 = prisoner2()

        # Initialize scores
        score1 = 0
        score2 = 0

        # Play all rounds
        if not n_rounds:
            n_rounds = self.n_rounds
        for n in range(n_rounds):
            strategy1 = p1.pick_strategy()
            strategy2 = p2.pick_strategy()
            scores = self.score(strategy1, strategy2)
            score1 += scores[0]
            score2 += scores[1]
            p1.process_results(strategy1, strategy2)
            p2.process_results(strategy2, strategy1)
            # print('(', strategy1, ',', strategy2, ')')

        # Return scores
        # print('puntajes: (', score1, ',', score2, ')')
        return score1, score2

    """
    Play a round robin tournament
    """

    def round_robin(self):

        # Create a list of all combinations of competing
        matches = list(combinations(range(len(self.competing)), 2))
        shuffle(matches)

        # Play all matches
        for match in matches:
            # print('estan jugando: ', self.competing[match[0]].__name__, " vs ", self.competing[match[1]].__name__)
            (score1, score2) = self.play_match(
                self.competing[match[0]],
                self.competing[match[1]])
            self.scores[match[0]] += score1
            self.scores[match[1]] += score2

    def get_winners_index(self):
        m = max(self.scores)
        winners = []
        for i in range(len(self.competing)):
            if self.scores[i] == m:
                winners.extend([i])

        return winners

    def get_winners_name(self):
        return list(map(lambda i: self.competing[i].name(), self.get_winners_index()))

    def results(self):
        return list(map(
            lambda i: {
                "name": self.competing[i].name(),
                "score": self.scores[i]
            },
            list(range(len(self.competing))))
        )

    def reset_tournament(self):
        self.scores = len(self.competing) * [0]


def run_round_robin_tournament(competing, n_rounds=50):
    t = Tournament(competing, n_rounds)
    t.round_robin()

    return t.results()
