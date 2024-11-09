from Prisoner import Prisoner
import math
import enum


class Strategy(enum.Enum):
    SIATODO = 1
    TWOTITFORTAT = 2
    ANTICADENAS = 3
    FALSE = 4
    TITFORTAT = 5


class TeammateDaleCooperReceiver(Prisoner):
    # "Harry, I'm going to let you in on a little secret. Every day, once a day,
    # give yourself a present. Don't plan it. Don't wait for it. Just let it happen.
    # It could be a new shirt at the men's store, a catnap in your office chair, or two cups of good,
    # hot black coffee."

    def __init__(self):
        self.name = "TeammateDaleCooperReceiver"
        self.treintaDeAnalisis = [False] * 30
        self.rondasPasadas = 0
        # Empezamos con la estrategia más estúpida
        self.strategy = Strategy.SIATODO

        # Para el tit for tat
        self.jugadaPreviaOponente = True
        self.jugadaAnteriorAPreviaOponente = True

        # Para la estrategia anticadenas
        self.vecesCooperadasSeguidas = 0
        self.vecesDisentidasOponente = 0
        self.jugadaADisentir = 0

        # AGREGAMOS PARA QUE SEA TEAMMATE
        self.code = [
            True, True, False, True, False, True, True, False, False, True,
            # True, False, True, False, True, True, False, True, True, True
        ]
        self.code_state = 0

    @staticmethod
    def name():
        return "TeammateDaleCooperReceiver"

    def pick_strategy(self):
        if self.code_state == -1:
            return self.actual_pick_strategy()

        # si todavia estoy cambiando el codigo, hago eso
        if self.code_state < len(self.code):
            # todavia estoy viendo si es mi aliado
            return self.code[self.code_state]
        elif self.code_state == len(self.code):
            # es mi aliado
            return False


    def actual_pick_strategy(self):
        # No tiene sentido cooperar si sabemos que es la última vez (este código funciona 1 de cada 300 veces)
        if (self.rondasPasadas == 399):
            return False
        # Si el oponente disiente después de cooperar una cantidad de veces, decidimos disentir antes.
        # No le ganamos pero si mantenemos casi todos los puntos que daría titfortat
        elif (self.strategy == Strategy.ANTICADENAS):
            if (self.jugadaADisentir == self.vecesCooperadasSeguidas):
                return False

            else:
                return True

        # El buen TwoTitForTat, nada le gana. Somos extra permisivos para analizar la estrategia ajena
        elif (self.strategy == Strategy.TWOTITFORTAT):
            return self.jugadaPreviaOponente or self.jugadaAnteriorAPreviaOponente
        # Si el oponente juega de forma aleatoria, siempre conviene disentir
        elif (self.strategy == Strategy.FALSE):
            return False
        # Las primeras veces cooperamos, por las dudas
        elif (self.strategy == Strategy.SIATODO):
            return True
        # El buen titfortat, nada le gana
        elif (self.strategy == Strategy.TITFORTAT):
            return self.jugadaPreviaOponente

    # Hacemos un análisis de todas las jugadas anteriores. ¿Conviene continuar haciendo TitForTat,
    # intentamos romper patrones de cooperación que use el rival, o simplemente lo tratamos como aleatorio?
    def change_strategy(self):
        cooperarConsecutivos = 0
        disentirConsecutivos = 0
        MaxDisentirConsecutivos = 0

        cadenaCooperacionPromedio = 0
        cadenasCooperacionAisladas = 0

        vecesDisentidas = 0
        vecesCooperadas = 0
        for i in range(0, len(self.treintaDeAnalisis)):
            if (self.treintaDeAnalisis[i] == False):
                disentirConsecutivos += 1
                vecesDisentidas += 1
                # cadenaCooperacionPromedio += cooperarConsecutivos
                if (cooperarConsecutivos != 0):
                    if (cooperarConsecutivos == 1):
                        cadenasCooperacionAisladas += 1
                    cooperarConsecutivos = 0


            elif (self.treintaDeAnalisis[i] == True):
                vecesCooperadas += 1
                cooperarConsecutivos += 1
                if (disentirConsecutivos != 0):
                    MaxDisentirConsecutivos = max(disentirConsecutivos, MaxDisentirConsecutivos)
                    disentirConsecutivos = 0
        # Si nunca disiente, pasamos a titForTat  que es óptima
        if (vecesDisentidas == 0):
            self.strategy = Strategy.TITFORTAT
        else:
            cadenaCooperacionPromedio = vecesCooperadas / (vecesDisentidas + 1)

            # Consideramos comportamientos incoherentes como prácticamente aleatorios, en particular
            # cadenas extrañas de cooperación y disentimiento
            if (MaxDisentirConsecutivos > 2 or (cadenasCooperacionAisladas > 1 and cadenaCooperacionPromedio < 3)
                    or (cadenasCooperacionAisladas > 2 > cadenaCooperacionPromedio)):
                self.strategy = Strategy.FALSE
            else:
                # Por las dudas, si se disentió pocas veces es dificil hacer un estimativo preciso
                if (vecesDisentidas < 3):
                    self.jugadaADisentir = 10
                else:
                    self.jugadaADisentir = math.floor(cadenaCooperacionPromedio)
                self.strategy = Strategy.ANTICADENAS

    def process_results(self, my_strategy, other_strategy):
        if self.code_state == -1:
            # si no es mi aliado, proceso normal
            self.actual_process_result(my_strategy, other_strategy)

        elif self.code_state < len(self.code):
            # todavia estoy viendo si es mi aliado
            if other_strategy == self.code[self.code_state]:
                self.code_state = self.code_state + 1
            else:
                self.code_state = -1

        elif self.code_state == len(self.code):
            # si ya se que es mi aliado
            pass

    def actual_process_result(self, my_strategy, other_strategy):
        # Las primeras 5 rondamos cooperamos siempre, para ver qué pasa
        if (self.rondasPasadas == 4):
            self.strategy = Strategy.TWOTITFORTAT
            self.jugadaPreviaOponente = other_strategy
        # Guardamos historial de jugadas para decidir qué hacer
        elif (self.rondasPasadas < 35):
            self.treintaDeAnalisis[self.rondasPasadas - 5] = other_strategy
        elif (self.rondasPasadas == 35):
            self.change_strategy()

        if (self.strategy == Strategy.TWOTITFORTAT):
            self.jugadaAnteriorAPreviaOponente = self.jugadaPreviaOponente
            self.jugadaPreviaOponente = other_strategy
        elif (self.strategy == Strategy.TITFORTAT):
            self.jugadaPreviaOponente = other_strategy
        elif (self.strategy == Strategy.ANTICADENAS):
            if (my_strategy == False):
                self.vecesCooperadasSeguidas = 0
            else:
                self.vecesCooperadasSeguidas += 1

            if (other_strategy == False):
                self.vecesDisentidasOponente += 1
                self.vecesCooperadasSeguidas = 0
                # Algo falló en mi razonamiento y anti cadenas ya no funciona. Probablemente
                # convenga continuar con titForTat para maximizar puntuación.
                if (self.vecesDisentidasOponente == 2):
                    self.strategy = Strategy.TITFORTAT
            else:
                self.vecesDisentidasOponente = 0
        self.rondasPasadas += 1
