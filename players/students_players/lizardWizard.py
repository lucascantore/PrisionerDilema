from Prisoner import Prisoner


class lizardWizard(Prisoner):

    def __init__(self):
        self.estrategy_paths = [[i, j, k] for i in [True, False] for j in [True, False] for k in [True, False]]
        self.current_path = 0
        self.current_estrategy = 0
        self.estrategy_payment = [[i, 0] for i in range(len(self.estrategy_paths))]
        self.training = True
        self.change = False
        self.newPayment = 0
        self.N = 0  # inicializo los totales
        self.name = "Lizard Wizard"  # nombre completo a imprimir

    @staticmethod
    def name():
        return "Lizard Wizard"

    def show_list(self):
        for i in self.estrategy_paths:
            print(i)

    def next_estrategy_not_trained(self):
        if (self.current_estrategy == 1 and self.current_path == len(self.estrategy_paths) - 1):
            self.current_estrategy += 1
            self.training = False

        elif (self.current_estrategy == 2):
            self.current_path += 1
            self.current_estrategy = 0
        else:
            self.current_estrategy += 1

        return self.estrategy_paths[self.current_path][self.current_estrategy]

    def next_estrategy_trained(self):
        if (self.current_estrategy == 2):
            self.estrategy_payment = sorted(self.estrategy_payment, key=lambda x: x[1])
            self.current_path = self.estrategy_payment[0][0]
            self.current_estrategy = 0
        else:
            self.current_estrategy += 1

        return self.estrategy_paths[self.current_path][self.current_estrategy]

    def pick_strategy(self):

        if (self.training):
            return self.next_estrategy_not_trained()

        return self.next_estrategy_trained()

    def process_results(self, my_strategy, other_strategy):
        self.N += 1
        if self.N == (len(self.estrategy_paths) * len(self.estrategy_paths[0])):
            self.training = not self.training

        if my_strategy and other_strategy:
            self.newPayment += 1
        elif not my_strategy and other_strategy:
            self.newPayment += 2
        elif my_strategy and not other_strategy:
            self.newPayment += -1
        else:
            self.newPayment += 0

        if self.current_estrategy == 2:
            self.estrategy_payment[self.current_path][1] = self.newPayment
            self.newPayment = 0
