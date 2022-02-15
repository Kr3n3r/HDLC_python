#pedir información sobre alumnos hasta que se introduzca '*'

if __name__ == '__main__':
    lista = [[] * 2 for i in range(1)]
    while True:
        nombre = input("Introduzca el nombre del alumno: ")
        if nombre == '*':
            break
        else:
            edad = input("Introduzca la edad: ")
        lista.append([nombre,int(edad)])
    print("Los alumnos mayores de edad son:")
    max = 0
    for i in range(1,len(lista)):
        if lista[i][1] >= 18:
            print(lista[i][0])
        if lista[i][1] >= max:
            max = lista[i][1]
    print("Los alumnos mayores son:")
    for i in range(1,len(lista)):
        if lista[i][1] == max:
            print(lista[i][0])