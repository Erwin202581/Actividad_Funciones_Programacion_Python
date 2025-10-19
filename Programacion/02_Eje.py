# Clase Calculadora 

class Calculadora:
    def __init__(self):
        pass

    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero no permitida."

calc = Calculadora()
print(f"5 + 3 = {calc.sumar(5, 3)}")
print(f"10 - 4 = {calc.restar(10, 4)}")
print(f"6 * 7 = {calc.multiplicar(6, 7)}")
print(f"20 / 5 = {calc.dividir(20, 5)}")
print(f"10 / 0 = {calc.dividir(10, 0)}")
