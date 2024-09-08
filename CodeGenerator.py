import random


class CodeGenerator:

    def __init__(self):
        pass

    def generate_code(self, length=20):

        code = []

        for i in range(length):
            r = random.randint(0, 9)
            if r <= 4:
                code.append(True)
            else:
                code.append(False)

        return code
