class Personaje():
    def __init__(self, vida, posicion, velocidad):
        self.vida=vida
        self.posicion=posicion
        self.velocidad=velocidad
    def recibir_ataque(self, quantity):
        self.vida -= quantity
        if self.vida <= 0:
            print(f"Has muerto!")
    def mover(self, direccion):
        self.posicion+=direccion*self.velocidad
class Soldado(Personaje):
    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque=ataque
    def atacar(self, Personaje):
        Personaje.recibir_ataque(self.ataque)
class Campesino(Personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha=cosecha
    def cosechar(self):
        return self.cosecha

soldier=Soldado(100,0,5,10)
villager=Campesino(100,0,2,20)
soldier.atacar(villager)
print(villager.vida)
