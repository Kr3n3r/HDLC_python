
class Cuenta():
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad
    def print_data(self):
        return print(f'El titular de la cuenta es {self.titular} y su saldo es de {self.cantidad}')

class Plazo_fijo(Cuenta):
    def __init__(self,titular,cantidad,plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo=plazo
        self.interes=interes
    def calcular_interes(self):
        return self.cantidad*self.interes/100
    def print_data(self):
        super().print_data()
        print(f'Además, tiene un interés de {self.interes}% que asciende a {self.calcular_interes()}')

class Caja_ahorro(Cuenta):
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)
    def print_data(self):
        super().print_data()

cuenta = Cuenta('alejandro mármol romero', 1000)
cajadeahorros = Caja_ahorro('alberto sánchez gómez', 1234)
cuentaplazofijo = Plazo_fijo('pade de familia', 1200, 10, 2)
cuenta.print_data()
cajadeahorros.print_data()
cuentaplazofijo.print_data()