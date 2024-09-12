# Ejemplo

# Deben importar Prisoner, y cualquier otra biblioteca estándar de las incluidas
# con Python 3 que necesiten, por ej. random si usaran aleatorios.
# Si por alguna razón importante necesitaran incluir otras, hablar con el docente.

from Prisoner import Prisoner


# Sigue la declaración de la clase con su nombre, que tiene que ser subclase de Prisoner.
# Una instancia de la misma será el jugador, y las variables propias que usen deben ser todos atributos de self.

class GoodBoy(Prisoner):

    # En __init__ va la inicialización que deseen, que se ejecutará antes de la "partida" 1
    # ante cada oponente; tener en cuenta que cuando pasan a competir con un nuevo oponente
    # se vuelve a ejecutar esta función, para arrancar desde 0.

    def __init__(self):
        self.name = "GoodBoy"  # nombre completo a imprimir

    @staticmethod
    def name():
        return "GoodBoy"

    """
    forgive: 
    state: state of automata    
    """

    # Esta función determina la estrategia a usar en cada ronda

    def pick_strategy(self):
        return True

    # Esta función procesa los resultados, y se llama después de cada "partida". Los parámetros son dos booleanos:
    # my_strategy = última estrategia usada por mí, other_strategy = última usada por el oponente.

    def process_results(self, my_strategy, other_strategy):
        pass
