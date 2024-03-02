# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Tournament import Tournament
from ElGuason import ElGuason
from GreedyWizard import GreedyWizard
from Random import Random
from Lucifer import Lucifer
from GreedyWizard2 import GreedyWizard2
from NotSoGreedyWizard import NotSoGreedyWizard

def run():
  competing = [ GreedyWizard, GreedyWizard2, NotSoGreedyWizard, Random]
  a = Tournament(competing,20)
  a.round_robin()
  print(a.scores)

  m=max(a.scores)
  winners=[]
  for i in range(len(competing)):
       if a.scores[i] == m:
         winners.extend([i])
  print("ganadores: ",winners)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
