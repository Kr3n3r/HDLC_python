
class cliente:
    def __init__(self,nombre:str,saldo:float):
        self.nombre=nombre
        self.saldo=saldo
    def setnombre(self,string):
        self.nombre = string
    def setsaldo(self, float):
        self.saldo = float
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
    def extraer(self, cantidad):
        self.saldo = self.saldo - cantidad
    def mostrar_total(self):
        return self.saldo

class banco():
    def __init__(self,cliente1,cliente2,cliente3):
        self.cliente1=cliente1
        self.cliente2=cliente2
        self.cliente3=cliente3
    def operar(self,pagador,deudador,cantidad):
        pagador.extraer(cantidad)
        deudador.depositar(cantidad)
        print(f"El cliente {pagador.nombre} ha depositado {cantidad} en la cuenta de {deudador.nombre}")
        print(f"Pago realizado correctamente")
    def deposito_total(self):
        return self.cliente1.mostrar_total() + self.cliente3.mostrar_total() + self.cliente3.mostrar_total() 

clienteA=cliente('A',1000)
clienteB=cliente('B',2000)
clienteC=cliente('C',3000)
banco_central=banco(clienteA,clienteB,clienteC)
banco_central.operar(clienteC, clienteA, 1000)
print(f'{clienteA.mostrar_total()}')
print(f'{clienteC.mostrar_total()}')
print(f'{banco_central.deposito_total()}')