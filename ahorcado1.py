import random

a=1
defecto='_'
diccionario = ["uno","doh","tre","siete"]
cont=0
palabra = random.choice(diccionario)
# esto está muy bien pensado a la hora de componer una lista
tablero = ['_'] * len(palabra)
 
print(tablero)
print (" ")

while True:
    letra = input("Elige una letra: ")
    for i in range(len(palabra)):
        if palabra[i] == letra:
            tablero[i] = letra
            cont += 1
    print(tablero)
    print("Has acertado",cont,"y te quedan",len(palabra)-cont)
    if cont == len(palabra):
        break

print("HAS GANADO")