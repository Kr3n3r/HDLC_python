# imprimir números pares entre x e y

num1=eval(input("Introduce el primer número: "))
num2=eval(input("Introduce el segundo número: "))
lista=list()

for i in range(num1,num2):
    if i%2 == 0:
        lista.append(i)
print("Los números pares son",lista)