class Persona():
    def ataca(self,Entity)
        Entity.salud -= self.ataque
        return True

class Soldado(Persona):
    salud = 100
    ataque = 25
class Mago(Persona):
    salud = 100
    ataque = 40
class Hada(Persona):
    salud = 100
    ataque = 32
class Rey(Persona):
    salud = 100
    ataque = 36
class Fuego(Persona):
    salud = 100
    ataque = 28

def main():
    SoldadoAzul = Soldado()
    MagoAzul = Mago()
    ReyAzul = Rey()
    FuegoAzul = Fuego()

    SoldadoRojo = Soldado()
    HadaRojo = Hada()
    ReyRojo = Rey()
    FuegoRojo = Fuego()

    while True:
        ReyAzul.ataca(SoldadoRojo)
        FuegoAzul.ataca(FuegoRojo)
        MagoAzul.ataca(ReyRojo)

        HadaRojo.ataca(FuegoAzul)
        ReyRojo.ataca(ReyAzul)

        if ReyAzul.salud <= 0:
            print("El equipo rojo ha ganado")
            return False
        
        if ReyRojo.salud <= 0:
            print("El equipo azul ha ganado")
            return False

main()