
class Calculadora():
    def __init__(self):
        self.integer1 = int(input("Introduzca el primer número: "))
        self.integer2 = int(input("Introduzca el segundo número: "))
    def suma(self):
        return self.integer1 + self.integer2
    def resta(self):
        return self.integer1 - self.integer2
    def multiplicacion(self):
        return self.integer1 * self.integer2
    def division(self):
        return self.integer1 / self.integer2

if __name__ == "__main__":
    calculadora = Calculadora()
    print(calculadora.suma())
    print(calculadora.resta())
    print(calculadora.multiplicacion())
    print(calculadora.division())