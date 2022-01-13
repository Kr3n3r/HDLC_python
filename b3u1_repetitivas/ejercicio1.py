# factorial sin funciones
num = int(input("Introduzca un número para calcular su factorial: "))
factorial=int(1)
for i in range(1,num+1):
 factorial = factorial*i
print("El factorial de",num,"es",factorial)