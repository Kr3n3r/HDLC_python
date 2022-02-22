
npartidos = 15
equipos = [[""] * 2 for i in range(npartidos)]
partidos = [[0] * 2 for i in range(npartidos)]

for i in range(npartidos):
    equipo1 = input("Introduzca el nombre del primer equipo: ")
    equipos[i][0] = equipo1
    resultado1 = input("Introduzca los goles del primer equipo: ")
    partidos[i][0] = int(resultado1)

    equipo2 = input("Introduzca el nombre del segundo equipo: ")
    equipos[i][1] = equipo2
    resultado2 = input("Introduzca los goles del primer equipo: ")
    partidos[i][1] = int(resultado2)
    
    
    # print(equipos[::][i])
    # print(partidos[::][i])
for i in range(npartidos):
    print(f"La quiniela es la siguiente:\n")
    print(f'{equipos[i][0]}-{equipos[i][1]} <-> {partidos[i][0]}-{partidos[i][1]}')