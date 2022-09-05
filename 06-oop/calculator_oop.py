class Calculator:

    # operator_2_bis = 0

    def __init__(self):
        self.operator_1 = float(input('Alege primul numar: '))
        self.operator_2 = float(input('Alege al doilea numar: '))
        self.semn = input('Alege semn: ')

    def adunare(self):
        return self.operator_1 + self.operator_2

    def scadere(self):
        return self.operator_1 - self.operator_2

    def inmultire(self):
        return self.operator_1 * self.operator_2

    def impartire(self):
        while self.operator_2 == 0.0:
            self.operator_2 = float(input('Alege din nou al doilea numar: '))
            if self.operator_2 != 0.0:
                break
        print(self.operator_2, '22')
        return self.operator_1 / self.operator_2

    def __str__(self):
        if self.semn == '+':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.adunare()}"
        elif self.semn == '-':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.scadere()}"
        elif self.semn == '*':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.inmultire()}"
        elif self.semn == '/':
            print(self.operator_2, '33')
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.impartire()}"
        else:
            return 'Operatia nu exista'


obiect_calculator = Calculator()
print(obiect_calculator)