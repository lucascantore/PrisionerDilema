# Decided to have this in a separate file because of all the imports

from players.students_players.AlCapone import AlCapone
from players.students_players.AndyDufresne import AndyDufresne
from players.students_players.avg_guy import AvgGuy
from players.students_players.BahHumbug import BahHumbug
from players.students_players.Bogo import Bogo
from players.students_players.ChuckBass import ChuckBass
from players.students_players.Collabotage import Collabotage
from players.students_players.Copion import Copion
from players.students_players.DaleCooper import DaleCooper
from players.students_players.DonRamon import DonRamon
from players.students_players.E_tit_for_2_tat import E_tit_for_2_tat
from players.students_players.ElAcertijo import ElAcertijo
from players.students_players.ElGrinch import ElGrinch
from players.students_players.ElGuason import ElGuason
from players.students_players.EstrategiaMacanuda import EstrategiaMacanuda
from players.students_players.Falco import Falco
from players.students_players.Familiero import Familiero
from players.students_players.FelizNavidad import FelizNavidad
from players.students_players.Gaston import Gaston
from players.students_players.GirlPower import GirlPower
from players.students_players.GreedyWizard import GreedyWizard
from players.students_players.IAndOTitForTat import IAndOTitForTat
from players.students_players.Ilan import Ilan
from players.students_players.Inv_Judas import Inv_Judas
from players.students_players.Jesus import Jesus
from players.students_players.JMR import JMR
from players.students_players.JohnTravolta import JohnTravolta
from players.students_players.Juan import Juan
from players.students_players.Judas2 import Judas2
from players.students_players.JugaCporfa import JugaCporfa
from players.students_players.Julieta import Julieta
from players.students_players.LAMBDANEITOR import LAMBDANEITOR
from players.students_players.Lasorsa import Lasorsa
from players.students_players.LionelHutz import LionelHutz
from players.students_players.lizardWizard import lizardWizard
from players.students_players.LosConfundidores import LosConfundidores
from players.students_players.Lucifer import Lucifer
from players.students_players.Lucifer735 import Lucifer735
from players.students_players.Lucy import Lucy
from players.students_players.Macho import Macho
from players.students_players.MalaOnda import MalaOnda
from players.students_players.Marx import Marx
from players.students_players.MasonPrisoner import MasonPrisoner
from players.students_players.MateConNueces import MateConNueces
from players.students_players.MichaelScofield import MichaelScofield
from players.students_players.Morning import Morning
from players.students_players.Nashville import Nashville
from players.students_players.Natan import Natan
from players.students_players.Nicolas import Nicolas
from players.students_players.Ninja import Ninja
from players.students_players.NoStrategy import NoStrategy
from players.students_players.Pablo import Pablo
from players.students_players.Pavlov import Pavlov
from players.students_players.PerdiBot import PerdiBot
from players.students_players.PetisoOrejudo import PetisoOrejudo
from players.students_players.PlayerMastermind import PlayerMastermind
from players.students_players.PrimoLejanoDeTitForTat import PrimoLejanoDeTitForTat
from players.students_players.PrisioneroNY import PrisioneroNY
from players.students_players.PrisonerJuli import PrisonerJuli
from players.students_players.Prueba import Prueba
from players.students_players.Ramona import Ramona
from players.students_players.Random import Random
from players.students_players.ReclusoFG import ReclusoFG
from players.students_players.Rencoroso import Rencoroso
from players.students_players.Roberto import Roberto
from players.students_players.RobinHood import RobinHood
from players.students_players.RolDeCanela import RolDeCanela
from players.students_players.Sebastian import Sebastian
from players.students_players.Secuencias import SecuenciasJusta
from players.students_players.Sirenita import Sirenita
from players.students_players.SoyPresoPolitico import SoyPresoPolitico
from players.students_players.Star import Star
from players.students_players.SuperConi import SuperConi
from players.students_players.SuperPrisoner import SuperPrisoner
from players.students_players.Surtipepa import Surtipepa
from players.students_players.Telepath import Telepath
from players.students_players.TFT import TFT
from players.students_players.TitForSomeTats import TitForSomeTats
from players.students_players.TitForTat import TitForTat
from players.students_players.TitForTat_Avg import TitForTat_Avg
from players.students_players.TitForTatConRandom import TitForTatConRandom
from players.students_players.TobiCM import TobiCM
from players.students_players.TraidorProbabilistico import TraidorProbabilistico
from players.students_players.TrustMe import TrustMe
from players.students_players.War import War
from players.students_players.Xerpa import Xerpa
from players.students_players.Zelig import Zelig
from players.teammates_lucifer.TeammateLuciferPointReceiver import TeammateLuciferPointReceiver
from players.teammates_lucifer.TeammateLuciferPointGiver import TeammateLuciferPointGiver
from players.teammates_tipfortat.TeammateTipForTatPointReceiver import TeammateTipForTatPointReceiver
from players.teammates_tipfortat.TeammateTipForTatPointGiver import TeammateTipForTatPointGiver
from players.teammate_dalecooper.TeammateDaleCooperReceiver import TeammateDaleCooperReceiver
from players.teammate_dalecooper.TeammateDaleCooperGiver import TeammateDaleCooperGiver
from players.teammate_natan.TeammateNatanReceiver import TeammateNatanReceiver
from players.teammate_natan.TeammateNatanGiver import TeammateNatanGiver

# importo las herramientas para experimentar
from experimentationTools import run_experiment_with, run_single_experiment_with, run_experiment_with_between


def run_experiment_with_students_players(max_rounds):
    run_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver,
         TeammateLuciferPointGiver, TeammateLuciferPointReceiver,
         AlCapone, AndyDufresne, AvgGuy, BahHumbug, Bogo, ChuckBass, Collabotage, Copion, DaleCooper, DonRamon,
         E_tit_for_2_tat, ElAcertijo, ElGrinch, ElGuason, EstrategiaMacanuda, Falco, Familiero, FelizNavidad,
         Gaston, GirlPower, GreedyWizard, IAndOTitForTat, Ilan, Inv_Judas, Jesus, JMR, JohnTravolta, Juan,
         Judas2, JugaCporfa, Julieta, LAMBDANEITOR, Lasorsa, LionelHutz, lizardWizard, LosConfundidores,
         Lucifer, Lucifer735, Lucy, Macho, Marx, MasonPrisoner, MateConNueces, MichaelScofield,
         Morning, Nashville, Natan, Nicolas, Ninja, NoStrategy, Pablo, Pavlov, PerdiBot, PetisoOrejudo,
         PlayerMastermind, PrimoLejanoDeTitForTat, PrisioneroNY, PrisonerJuli, Prueba, Ramona, Random,
         ReclusoFG, Rencoroso, Roberto, RobinHood, RolDeCanela, Sebastian,
         SecuenciasJusta, Sirenita, SoyPresoPolitico, Star, SuperConi, SuperPrisoner, Surtipepa,
         Telepath, TFT, TitForSomeTats, TitForTat, TitForTat_Avg, TitForTatConRandom, TobiCM,
         TraidorProbabilistico, TrustMe, War, Xerpa, Zelig
         ],
        max_rounds,
        "experiment_results/17_all-out-war.xlsx"
    )


def run_experiment_with_student_players_and_teammate_dale_cooper(max_rounds):
    run_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver,
         TeammateLuciferPointGiver, TeammateLuciferPointReceiver,
         TeammateDaleCooperGiver, TeammateDaleCooperReceiver,
         AlCapone, AndyDufresne, AvgGuy, BahHumbug, Bogo, ChuckBass, Collabotage, Copion, DaleCooper, DonRamon,
         E_tit_for_2_tat, ElAcertijo, ElGrinch, ElGuason, EstrategiaMacanuda, Falco, Familiero, FelizNavidad,
         Gaston, GirlPower, GreedyWizard, IAndOTitForTat, Ilan, Inv_Judas, Jesus, JMR, JohnTravolta, Juan,
         Judas2, JugaCporfa, Julieta, LAMBDANEITOR, Lasorsa, LionelHutz, lizardWizard, LosConfundidores,
         Lucifer, Lucifer735, Lucy, Macho, Marx, MasonPrisoner, MateConNueces, MichaelScofield,
         Morning, Nashville, Natan, Nicolas, Ninja, NoStrategy, Pablo, Pavlov, PerdiBot, PetisoOrejudo,
         PlayerMastermind, PrimoLejanoDeTitForTat, PrisioneroNY, PrisonerJuli, Prueba, Ramona, Random,
         ReclusoFG, Rencoroso, Roberto, RobinHood, RolDeCanela, Sebastian,
         SecuenciasJusta, Sirenita, SoyPresoPolitico, Star, SuperConi, SuperPrisoner, Surtipepa,
         Telepath, TFT, TitForSomeTats, TitForTat, TitForTat_Avg, TitForTatConRandom, TobiCM,
         TraidorProbabilistico, TrustMe, War, Xerpa, Zelig
         ],
        max_rounds,
        "experiment_results/18_all-out-war-with-teammate-dale-cooper.xlsx"
    )


def test_all_out_war_with_less_participants(max_rounds):
    run_experiment_with(
        [  # TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver,
            # TeammateLuciferPointGiver, TeammateLuciferPointReceiver,
            TeammateDaleCooperGiver, TeammateDaleCooperReceiver,
            AlCapone, AndyDufresne, AvgGuy, BahHumbug, Bogo, ChuckBass, Collabotage, Copion, DaleCooper, DonRamon,
            # E_tit_for_2_tat, ElAcertijo, ElGrinch, ElGuason, EstrategiaMacanuda, Falco, Familiero, FelizNavidad,
            Gaston, GirlPower, GreedyWizard, IAndOTitForTat, Ilan, Inv_Judas, Jesus, JMR, JohnTravolta, Juan,
            # Judas2, JugaCporfa, Julieta, LAMBDANEITOR, Lasorsa, LionelHutz, lizardWizard, LosConfundidores,
            Lucifer, Lucifer735, Lucy, Macho, Marx, MasonPrisoner, MateConNueces, MichaelScofield,
            # Morning, Nashville, Natan, Nicolas, Ninja, NoStrategy, Pablo, Pavlov, PerdiBot, PetisoOrejudo,
            PlayerMastermind, PrimoLejanoDeTitForTat, PrisioneroNY, PrisonerJuli, Prueba, Ramona, Random,
            # ReclusoFG, Rencoroso, Roberto, RobinHood, RolDeCanela, Sebastian,
            SecuenciasJusta, Sirenita, SoyPresoPolitico, Star, SuperConi, SuperPrisoner, Surtipepa,
            # Telepath, TFT, TitForSomeTats, TitForTat, TitForTat_Avg, TitForTatConRandom, TobiCM,
            # TraidorProbabilistico, TrustMe, War, Xerpa, Zelig
        ],
        max_rounds,
        "experiment_results/18_all-out-war-with-less-participants.xlsx"
    )


def test_all_out_war_single_tournament(n_rounds):
    run_single_experiment_with(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver,
         TeammateLuciferPointGiver, TeammateLuciferPointReceiver,
         TeammateDaleCooperGiver, TeammateDaleCooperReceiver,
         AlCapone, AndyDufresne, AvgGuy, BahHumbug, Bogo, ChuckBass, Collabotage, Copion, DaleCooper, DonRamon,
         E_tit_for_2_tat, ElAcertijo, ElGrinch, ElGuason, EstrategiaMacanuda, Falco, Familiero, FelizNavidad,
         Gaston, GirlPower, GreedyWizard, IAndOTitForTat, Ilan, Inv_Judas, Jesus, JMR, JohnTravolta, Juan,
         Judas2, JugaCporfa, Julieta, LAMBDANEITOR, Lasorsa, LionelHutz, lizardWizard, LosConfundidores,
         Lucifer, Lucifer735, Lucy, Macho, Marx, MasonPrisoner, MateConNueces, MichaelScofield,
         Morning, Nashville, Natan, Nicolas, Ninja, NoStrategy, Pablo, Pavlov, PerdiBot, PetisoOrejudo,
         PlayerMastermind, PrimoLejanoDeTitForTat, PrisioneroNY, PrisonerJuli, Prueba, Ramona, Random,
         ReclusoFG, Rencoroso, Roberto, RobinHood, RolDeCanela, Sebastian,
         SecuenciasJusta, Sirenita, SoyPresoPolitico, Star, SuperConi, SuperPrisoner, Surtipepa,
         Telepath, TFT, TitForSomeTats, TitForTat, TitForTat_Avg, TitForTatConRandom, TobiCM,
         TraidorProbabilistico, TrustMe, War, Xerpa, Zelig
         ],
        n_rounds,
        "experiment_results/18_all-out-war-wingle.xlsx"
    )


def test_all_out_war_high_numbers(n_rounds_start, n_rounds_finish):
    run_experiment_with_between(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver,
         TeammateLuciferPointGiver, TeammateLuciferPointReceiver,
         TeammateDaleCooperGiver, TeammateDaleCooperReceiver,
         AlCapone, AndyDufresne, AvgGuy, BahHumbug, Bogo, ChuckBass, Collabotage, Copion, DaleCooper, DonRamon,
         E_tit_for_2_tat, ElAcertijo, ElGrinch, ElGuason, EstrategiaMacanuda, Falco, Familiero, FelizNavidad,
         Gaston, GirlPower, GreedyWizard, IAndOTitForTat, Ilan, Inv_Judas, Jesus, JMR, JohnTravolta, Juan,
         Judas2, JugaCporfa, Julieta, LAMBDANEITOR, Lasorsa, LionelHutz, lizardWizard, LosConfundidores,
         Lucifer, Lucifer735, Lucy, Macho, Marx, MasonPrisoner, MateConNueces, MichaelScofield,
         Morning, Nashville, Natan, Nicolas, Ninja, NoStrategy, Pablo, Pavlov, PerdiBot, PetisoOrejudo,
         PlayerMastermind, PrimoLejanoDeTitForTat, PrisioneroNY, PrisonerJuli, Prueba, Ramona, Random,
         ReclusoFG, Rencoroso, Roberto, RobinHood, RolDeCanela, Sebastian,
         SecuenciasJusta, Sirenita, SoyPresoPolitico, Star, SuperConi, SuperPrisoner, Surtipepa,
         Telepath, TFT, TitForSomeTats, TitForTat, TitForTat_Avg, TitForTatConRandom, TobiCM,
         TraidorProbabilistico, TrustMe, War, Xerpa, Zelig
         ],
        n_rounds_start,
        n_rounds_finish,
        "experiment_results/18_all-out-war-wingle_high.xlsx"
    )


def test_all_out_war_high_numbers_and_nathan(n_rounds_start, n_rounds_finish):
    run_experiment_with_between(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver,
         TeammateLuciferPointGiver, TeammateLuciferPointReceiver,
         TeammateDaleCooperGiver, TeammateDaleCooperReceiver,
         TeammateNatanGiver, TeammateNatanReceiver,
         AlCapone, AndyDufresne, AvgGuy, BahHumbug, Bogo, ChuckBass, Collabotage, Copion, DaleCooper, DonRamon,
         E_tit_for_2_tat, ElAcertijo, ElGrinch, ElGuason, EstrategiaMacanuda, Falco, Familiero, FelizNavidad,
         Gaston, GirlPower, GreedyWizard, IAndOTitForTat, Ilan, Inv_Judas, Jesus, JMR, JohnTravolta, Juan,
         Judas2, JugaCporfa, Julieta, LAMBDANEITOR, Lasorsa, LionelHutz, lizardWizard, LosConfundidores,
         Lucifer, Lucifer735, Lucy, Macho, Marx, MasonPrisoner, MateConNueces, MichaelScofield,
         Morning, Nashville, Natan, Nicolas, Ninja, NoStrategy, Pablo, Pavlov, PerdiBot, PetisoOrejudo,
         PlayerMastermind, PrimoLejanoDeTitForTat, PrisioneroNY, PrisonerJuli, Prueba, Ramona, Random,
         ReclusoFG, Rencoroso, Roberto, RobinHood, RolDeCanela, Sebastian,
         SecuenciasJusta, Sirenita, SoyPresoPolitico, Star, SuperConi, SuperPrisoner, Surtipepa,
         Telepath, TFT, TitForSomeTats, TitForTat, TitForTat_Avg, TitForTatConRandom, TobiCM,
         TraidorProbabilistico, TrustMe, War, Xerpa, Zelig
         ],
        n_rounds_start,
        n_rounds_finish,
        "experiment_results/18_all-out-war-high-with-natan2.xlsx"
        # todo sacarle el 2, y analizar que pasa si pasa de 1000 rondas
    )


def test_all_out_war_with_less_randomness(n_rounds_start, n_rounds_finish):
    run_experiment_with_between(
        [TeammateTipForTatPointGiver, TeammateTipForTatPointReceiver,
         TeammateLuciferPointGiver, TeammateLuciferPointReceiver,
         TeammateDaleCooperGiver, TeammateDaleCooperReceiver,
         TeammateNatanGiver, TeammateNatanReceiver,
         AlCapone, AndyDufresne, AvgGuy, DaleCooper,
         E_tit_for_2_tat, ElAcertijo, EstrategiaMacanuda, Familiero,
         Gaston, GirlPower, GreedyWizard, Inv_Judas, Jesus, JohnTravolta,
         Judas2, JugaCporfa, lizardWizard, LosConfundidores,
         Lucifer, Lucy, MichaelScofield,
         Morning, Natan, Pablo, Pavlov, PerdiBot, PetisoOrejudo,
         PlayerMastermind, PrimoLejanoDeTitForTat, PrisonerJuli,
         ReclusoFG, Rencoroso, RolDeCanela, Sebastian,
         SoyPresoPolitico, Star, SuperConi,
         Telepath, TFT, TitForSomeTats, TitForTat, TitForTat_Avg,
         War, Zelig
         ],
        n_rounds_start,
        n_rounds_finish,
        f"experiment_results/18_all-out-war-with-less-randomness-from-{n_rounds_start}-to-{n_rounds_finish}.xlsx"
    )
