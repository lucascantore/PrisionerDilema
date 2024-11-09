# Ejemplo

# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner


# Sigue la declaración de la clase con su nombre, que tiene que ser subclase de Prisoner.
# Una instancia de la misma será el jugador, y las variables propias que usen deben ser todos atributos de self.

class PrimoLejanoDeTitForTat(Prisoner):

    # En __init__ va la inicialización que deseen, que se ejecutará antes de la "partida" 1
    # ante cada oponente; tener en cuenta que cuando pasan a competir con un nuevo oponente
    # se vuelve a ejecutar esta función, para arrancar desde 0.

    def __init__(self):
        self.N = 0
        self.name = "PrimoLejanoDeTitForTat"  # nombre completo a imprimir
        self.oponent_history = []
        self.my_history = []
        self.strategies = {}

    @staticmethod
    def name():
        return "PrimoLejanoDeTitForTat"

    """
    N : nro. total de rondas hasta ahora
    C : cantidad de veces que cooperé
    ci : nro. total de veces seguidas que cooperé
    eC : nro. total de veces seguidas que el (mismo) oponente cooperó
    """

    # Esta función determina la estrategia a usar en cada ronda, pudiendo mirar cualquier
    # atributo propio del objeto definido como jugador, en este caso ElGuason.

    def pick_strategy(self):
        if self.N == 0:
            return False  # coopero en la primera ronda
        elif self.N == 1:
            return self.oponent_history[0] == 1  # copio lo que hizo el oponente en la primera ronda
        else:
            p = 0
            for i in range(1, min(self.N, 6)):
                s = tuple(self.my_history[-i - 1:-1])
                p += self.strategies[s] * i  # quiza tenga que modificar los pesos
            return p > 0

    def process_results(self, my_strategy, other_strategy):
        self.N += 1

        self.my_history.append(my_strategy)
        self.oponent_history.append(other_strategy)

        if self.N > 1:
            for i in range(1, 6):
                s = tuple(self.my_history[-i - 1:-1])
                if s and len(s) == i:
                    if s not in self.strategies:
                        self.strategies[s] = 0
                    self.strategies[s] = self.strategies[s] + 1 if other_strategy else self.strategies[s] - 1
