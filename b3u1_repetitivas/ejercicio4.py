# pide números y guarda los mayores, menores e iguales a cero
num=int()
resultados={
    "mayores":0,
    "menores":0,
    "iguales":0
}

i=int(input("Introduce los números que vas a introducir: "))
while i != 10:
    num=int(input("Introduce un número: "))
    if num > 0:
        resultados["mayores"]+=1
    elif num < 0:
        resultados["menores"]+=1
    elif num == 0:
        resultados["iguales"]+=1
    i+=1

print(resultados)