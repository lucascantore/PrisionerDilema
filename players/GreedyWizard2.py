# Ejemplo

# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner


# Sigue la declaración de la clase con su nombre, que tiene que ser subclase de Prisoner.
# Una instancia de la misma será el jugador, y las variables propias que usen deben ser todos atributos de self.

class GreedyWizard2(Prisoner):

    # En __init__ va la inicialización que deseen, que se ejecutará antes de la "partida" 1
    # ante cada oponente; tener en cuenta que cuando pasan a competir con un nuevo oponente
    # se vuelve a ejecutar esta función, para arrancar desde 0.

    def __init__(self):
        self.name = "GreedyWizard2"  # nombre completo a imprimir

        self.forgive = True
        self.state = "A"
        self.timeStuck = 0

    @staticmethod
    def name():
        return "GreedyWizard2"

    """
    forgive: 
    state: state of automata    
    """

    # Esta función determina la estrategia a usar en cada ronda

    def pick_strategy(self):

        if self.state == 'A':
            return True
        elif self.state == 'B':
            return True
        elif self.state == 'C':
            return False
        elif self.state == 'D':
            return True
        elif self.state == 'E':
            return False

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    def process_results(self, my_strategy, other_strategy):

        if self.state == 'A':
            self.state = 'B'

        elif self.state == 'B':
            if other_strategy:
                self.state = 'C'
            else:
                self.state = 'E'

        elif self.state == 'C':
            if other_strategy:
                self.state = 'D'
            else:
                self.state = 'E'

        elif self.state == 'D':
            if other_strategy:
                self.state = 'B'
            else:
                self.state = 'C'

        elif self.state == 'E':
            if other_strategy:
                self.state = 'B'
                self.forgive = True
            else:
                if self.timeStuck > 7 and self.forgive:
                    self.forgive = False
                    self.timeStuck = 0
                    self.state = 'D'
                else:
                    self.timeStuck += 1
