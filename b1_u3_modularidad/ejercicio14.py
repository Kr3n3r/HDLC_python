
def InicializarPila():
    for i in range(0,9):
        pila[i] = '*'
    return pila

def LongitudPila(pila):
    return len(pila)

def EstaVaciaPila(pila):
    for i in range(0,9):
        if pila[i] != '':
            return False
    return True

def AddPila(str,pila):
    for i in range(0,9):
        if pila[i] == '':
            pila.append(str)
            return pila
    return print("Esta pila está llena")

pila = InicializarPila()
print(LongitudPila(pila))