from Prisoner import Prisoner
from random import randint

class LAMBDANEITOR(Prisoner):
    def __init__(self):
        self.name = "LAMBDANEITOR"
        self.c = True
        self.d = False
        self.state = self.First()
        self.enemy_history = []

    @staticmethod
    def name():
        return "LAMBDANEITOR"

    def pick_strategy(self):
        return self.state.next()

    def process_results(self, my_strategy, other_strategy):
        self.enemy_history.append(other_strategy)
        self.state = self.state.update(my_strategy, other_strategy, self.enemy_history)

    class State:
        def __init__(self):
            self.c = True
            self.d = False
        def next(self):
            pass
        def update(self, me, enemy, enemy_history):
            pass

    class First(State):
        def __init__(self):
            super().__init__()

        def next(self):
            super().__init__()
            return self.d

        def update(self, me, enemy, enemy_history):
            if me == self.c and enemy == self.c:
                return LAMBDANEITOR.Coop()
            elif me == self.d and enemy == self.c:
                return LAMBDANEITOR.Won()
            elif me == self.c and enemy == self.d:
                return LAMBDANEITOR.Lost()
            elif me == self.d and enemy == self.d:
                return LAMBDANEITOR.Nash()

    class Coop(State):
        def __init__(self):
            super().__init__()
            self.limit = randint(1,5)

        def next(self):
            if self.limit > 0:
                return self.c
            else:
                return self.d

        def update(self, me, enemy, enemy_history):
            if me == self.c and enemy == self.c:
                self.limit -= 1
                return self
            elif me == self.d and enemy == self.c:
                return LAMBDANEITOR.Won()
            elif me == self.c and enemy == self.d:
                return LAMBDANEITOR.Lost()
            elif me == self.d and enemy == self.d:
                return LAMBDANEITOR.Nash()

    class Won(State):
        def __init__(self):
            super().__init__()

        def next(self):
            return self.d

        def update(self, me, enemy, enemy_history):
            if me == self.d and enemy == self.c:
                return self
            elif me == self.d and enemy == self.d:
                return LAMBDANEITOR.Nash()

    class Lost(State):
        def __init__(self):
            super().__init__()

        def next(self):
            return self.d

        def update(self, me, enemy, enemy_history):
            if me == self.d and enemy == self.c:
                return LAMBDANEITOR.Won()
            elif me == self.d and enemy == self.d:
                return LAMBDANEITOR.Nash()

    class Nash(State):
        def __init__(self):
            super().__init__()
            self.count = 0
            self.attempt = randint(5,15)
            self.attempted = False

        def next(self):
            if self.count == self.attempt:
                return self.c
            else:
                return self.d

        def update(self, me, enemy, enemy_history):
            if self.c in enemy_history:
                self.count += 1
            if me == self.c and enemy == self.c:
                return LAMBDANEITOR.Coop()
            elif me == self.d and enemy == self.c:
                return LAMBDANEITOR.Hope()
            elif me == self.c and enemy == self.d:
                return self
            elif me == self.d and enemy == self.d:
                return self

    class Hope(State):
        def __init__(self):
            super().__init__()

        def next(self):
            return self.c

        def update(self, me, enemy, enemy_history):
            if me == self.c and enemy == self.c:
                return LAMBDANEITOR.Coop()
            elif me == self.c and enemy == self.d:
                return LAMBDANEITOR.Lost()
