# mostrar tabla de un número introducido
num = int(input("Introduzca un número para mostrar la tabla de multiplicar: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
print("Programa terminado")