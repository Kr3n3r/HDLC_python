# rellenar una matriz 10x10 de "X"

casillas = 10
tablero = [["putito"] * casillas for i in range(casillas)]

tablero[1][8] = "J"

for i in range(casillas):
    print (tablero[i])
