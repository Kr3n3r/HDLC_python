# rellenar una matriz 10x10 de "X"

# casillas = 10
# tablero = [["putito"] * casillas for i in range(casillas)]

# tablero[1][8] = "J"

# for i in range(casillas):
#     print (tablero[i])

columnas = 2
filas = 3
tabla2x3 = [["_"]*columnas for i in range(filas)]
tabla2x3[1][1] = "VOID"
tabla2x3[2][0] = "DIOV"
for i in range(filas):
    print(tabla2x3[i])
print(tabla2x3)
banana=['foo','apple','apPle']
banana.__delitem__(2)
print(banana)