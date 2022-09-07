# object name = obiect_calculator
# class name = Calculator
# property =
# activity = adunare, scadere, inmultire, impartire
class Calculator:

    def __init__(self):
        self.operator_1 = self.validate_string(input('Alege primul numar: '))
        self.operator_2 = self.validate_string(input('Alege al doilea numar: '))
        self.semn = self.validate_sign(input('Alege semn: '))
        if self.operator_2 == 0.0 and self.semn == '/':
            self.operator_2 = self.validate_zero_division()

    def validate_string(self, operator):
        while operator.isdigit() is False:
            operator = input("Alege din nou numarul: ")
        return float(operator)

    def validate_sign(self, semn):
        while semn not in ['+', '-', '*', '/']:
            semn = input('Alege semn: ')
        return semn

    def validate_zero_division(self):
        while self.operator_2 == 0.0:
            self.operator_2 = float(input('Alege din nou al doilea numar: '))
        return self.operator_2

    def adunare(self):
        return self.operator_1 + self.operator_2

    def scadere(self):
        return self.operator_1 - self.operator_2

    def inmultire(self):
        return self.operator_1 * self.operator_2

    def impartire(self):
        return self.operator_1 / self.operator_2

    def __str__(self):
        if self.semn == '+':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.adunare()}"
        elif self.semn == '-':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.scadere()}"
        elif self.semn == '*':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.inmultire()}"
        elif self.semn == '/':
            return f"{self.operator_1} {self.semn} {self.operator_2} = {self.impartire()}"
        else:
            return 'Operatia nu exista'


obiect_calculator = Calculator()
print(obiect_calculator)
