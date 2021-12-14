# script ejemplo en python que pide edad y determina si eres mayor de edad
import math

if __name__ == '__main__':
    edad=int(input("Introduzca su edad "))

    if edad >= 18 :
        print("Eres mayor de edad!")

    print("Programa terminado")
else:
    print("este no es el bloque principal")
