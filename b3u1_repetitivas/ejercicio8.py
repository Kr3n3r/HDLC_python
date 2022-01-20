import os
lim_inferior=-1
lim_superior=-2
numero=1
suma=0
out=0
equal=0

while lim_inferior>lim_superior:
    os.system("clear")
    lim_inferior=eval(input("Introduce el límite inferior del intervalo: "))
    lim_superior=eval(input("Introduce el límite superior del intervalo: "))

while True:
    numero = eval(input("Introduzca un número: "))
    suma+=numero
    if numero == 0:
        break
    elif numero>lim_superior & numero<lim_inferior:
        out+=1
    elif numero==lim_superior | numero==lim_inferior:
        equal+=1
    os.system("clear")

print("La suma es",suma)
print("Has introducido",out,"números fuera del intervalo")
print("Has introducido",equal,"iguales a los límites del intervalo")
