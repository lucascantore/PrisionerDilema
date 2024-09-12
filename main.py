# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Tournament import Tournament
from players.Random import Random
from players.GoodBoy import GoodBoy
from players.GreedyWizard import GreedyWizard
from players.GreedyWizard2 import GreedyWizard2
from utils.CodeGenerator import CodeGenerator

from players.Lucifer import Lucifer
from players.teammates_lucifer.TeammateLuciferPointGiver import TeammateLuciferPointGiver
from players.teammates_lucifer.TeammateLuciferPointReceiver import TeammateLuciferPointReceiver

from players.TipForTat import TipForTat
from players.teammates_tipfortat.TeammateTipForTatPointGiver import TeammateTipForTatPointGiver
from players.teammates_tipfortat.TeammateTipForTatPointReceiver import TeammateTipForTatPointReceiver
from Tournament import run_round_robin_tournament
from experimentation import run_all_experiments


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_all_experiments()
