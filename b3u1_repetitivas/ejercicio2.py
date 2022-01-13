# juego de adivinar un número
from random import *
sol=randint(1,100)
user_input=int(0)
intentos_restantes=9
while user_input != sol:
    user_input=int(input("Introduce un número hasta adivinar la solución: "))
    if user_input == sol:
        print("Has acertado!")
        print("El número de intentos_restantes fue",10-intentos_restantes)
        break
    elif user_input > sol:
        print("El número a acertar es menor que el introducido")
        print("Te quedan",intentos_restantes,"intentos_restantes")
        intentos_restantes-=1
    elif user_input < sol:
        print("El número a acertar es mayor que el introducido")
        print("Te quedan",intentos_restantes,"intentos_restantes")
        intentos_restantes-=1
    if intentos_restantes == 0:
        print("No te quedan más intentos_restantes")
        print("El número a acertar era",sol)
        break