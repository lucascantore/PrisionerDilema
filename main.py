# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Tournament import Tournament
from players.Random import Random
from players.GoodBoy import GoodBoy
from CodeGenerator import CodeGenerator

from players.Lucifer import Lucifer
from players.teammates_lucifer.TeammateLuciferPointGiver import TeammateLuciferPointGiver
from players.teammates_lucifer.TeammateLuciferPointReceiver import TeammateLuciferPointReceiver

from players.TipForTat import TipForTat
from players.teammates_tipfortat.TeammateTipForTatPointGiver import TeammateTipForTatPointGiver
from players.teammates_tipfortat.TeammateTipForTatPointReceiver import TeammateTipForTatPointReceiver


def run_tournament():
    competing = [
        TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver,
        TeammateLuciferPointGiver, TeammateLuciferPointReceiver,
    ]
    t = Tournament(competing, 2000)
    t.round_robin()
    print(t.scores)

    m = max(t.scores)
    winners = []
    for i in range(len(competing)):
        if t.scores[i] == m:
            winners.extend([i])

    print("Ganadores: ")
    for w in winners:
        print(competing[w].__name__)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(CodeGenerator().generate_code(20))
    run_tournament()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
