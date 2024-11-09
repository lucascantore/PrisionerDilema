from Prisoner import Prisoner
import random

"""
El research hecho para llegar a esta version con Reinforcement Learning del codigo se hizo con:
- The Prisoners Dilemma, Memory, and the Early Evolution of Intelligence: https://cse.msu.edu/~dolsonem/pdfs/prisoners_dilemma_memory.pdf
- Strategies for the Iterated Prisoner's Dilemma (Arxiv): https://arxiv.org/pdf/2111.11561 
- Iterated Prisoner's Dilemma: Definition, Example, Strategies: https://www.investopedia.com/terms/i/iterated-prisoners-dilemma.asp
- New Winning Strategies for the Iterated Prisoner's Dilemma: https://www.jasss.org/20/4/12.html
- Prisoner’s Dilemma Revisited: https://medium.com/@metaform3d/prisoners-dilemma-revisited-bfdaa0e02c80 
- Strategies for the Iterated Prisoner's Dilemma (Stanford): https://plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html 
"""


class MichaelScofield(Prisoner):
    def __init__(self):
        self.name = "MichaelScofield"
        # Estos parametros son los que deberian optimizar mi modelo
        self.learning_rate = 0.1
        self.discount_factor = 0.9  # que tan importantes son los rewards futuros
        self.exploration_rate = 0.1
        self.history_length = 10  # ponele que es un moving average de 10
        self.quality_table = {}
        self.history = []

    @staticmethod
    def name():
        return "MichaelScofield"

    def get_state(self):
        # Un "estado" esta representado como una tupla con los ultimos 10 movimientos registrados del oponente
        if len(self.history) < self.history_length:
            # si todavia no hay una cantidad que llegue al moving average limit entonces rellena con vacio
            return tuple(self.history + [''] * (self.history_length - len(self.history)))
        else:
            # caso contrario, me agarro los ultimos n elementos (n = moving average limit)
            return tuple(self.history[-self.history_length:])

    def pick_strategy(self):
        """
        De vez en cuando la estrategia que tomo la randomizo para no caer en algun ciclo
        """
        if random.random() < self.exploration_rate:
            if random.choice(['C', 'D']) == 'C':
                return True
            else:
                return False
        else:
            """
            En el caso que no randomizo mi eleccion:
            Si ya pase por el estado actual (esta en mi registro de estados), devuelvo C o D segun la calidad de Cooperar o Disentir
            Si no existe un estado tal, entonces asumo que ambas opciones tienen la misma calidad y devuelvo Disentir
            """
            state = self.get_state()
            quality_values = self.quality_table.get(state, {'C': 0, 'D': 0})
            return True if quality_values['C'] > quality_values['D'] else False

    def process_results(self, my_strategy, other_strategy):
        """
        Actualizo la historia de jugadas del oponente y actualizo los valores de calidad del estado actual
        """
        # Los rewards son los puntos determinados por el Tournament, no se si es lo que mejor maximiza la representacion de la calidad
        if my_strategy and other_strategy:
            reward = 1
        elif not my_strategy and other_strategy:
            reward = 2
        elif my_strategy and not other_strategy:
            reward = -1
        else:
            reward = 0

        state = self.get_state()
        move = my_strategy

        # Actualizo la historia para conseguir el estado luego de haber jugado
        self.history.append(other_strategy)
        if len(self.history) > self.history_length:
            self.history.pop(0)

        """
        next_state es el estado en el que va a estar mi jugador despues de haber tomado una decision
        """
        next_state = self.get_state()

        quality_values = self.quality_table.setdefault(state, {'C': 0, 'D': 0})
        next_quality_values = self.quality_table.setdefault(next_state, {'C': 0, 'D': 0})

        """
        por cada elemento de next_quality_values me fijo su valor de calidad y obtengo el maximo total
        """
        best_next_action = max(next_quality_values, key=next_quality_values.get)

        """
        Los valores de calidad determinan que tan bueno es elegir C o D dependiendo de un estado
        """
        quality_values[move] = quality_values.get(move, 0) + self.learning_rate * (
                    reward + self.discount_factor * next_quality_values[best_next_action] - quality_values.get(move, 0))
        self.quality_table[state] = quality_values
