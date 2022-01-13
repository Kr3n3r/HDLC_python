# algoritmo que pide números hasta que se introduce el 0
# e imprime suma y media
num=1
suma=int()
media=list()

while num != 0:
    num=int(input("Introduce un número: "))
    if num != 0:
        suma=suma + num
        media.append(num)

media=suma/len(media)
print("La suma de los números es",suma)
print("La media de los números es",media)
