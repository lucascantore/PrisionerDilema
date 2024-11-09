"""
Prisoner superclass
"""


class Prisoner():
    """
        Constructor. Called once at the start of each match.
        If needed, override this method to initialize any
        auxiliary data you want to use to determine your
        Prisoner's strategy. This data will persist between
        rounds of a match but not between matches.
        """

    def __init__(self):
        pass

    """
        Pick a strategy: return True to cooperate; return False to defect.
        If not overridden, the Prisoner will always cooperate.
        """

    def pick_strategy(self):
        return True

    """
        Process the results of a round. This provides an opportunity to
        store data that preserves memory of previous rounds.

        Parameters
        ----------
        my_strategy: bool
            This Prisoner's strategy

        other_strategy: bool
            The opponent's strategy
        """

    def process_results(self, my_strategy, other_strategy):
        pass

    @staticmethod
    def name():
        pass


def create_dynamic_prisoner_class(base_prisoner, prisoner_name):
    # Define a new static method for the dynamically created class
    def name():
        return prisoner_name

    # Create a new class with a custom name and a unique name() static method
    return type(
        prisoner_name,  # Name of the class
        (base_prisoner,),  # Base class tuple
        {'name': staticmethod(name)}  # Attributes, including the new static method
    )
