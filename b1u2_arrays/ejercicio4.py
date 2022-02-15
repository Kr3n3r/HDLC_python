# introducir enteros en un vecto de 10 elementos

vector = []
while len(vector)<10:
    num=int(input("Introduce un número en el vector: "))
    if num < 0 :
        break
    vector.append(num)
print(vector)