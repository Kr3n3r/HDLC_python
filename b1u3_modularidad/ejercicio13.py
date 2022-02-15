from math import gcd

def Leer_fraccion():
    numerador = int(input("Introduzca el numerador: "))
    denominador = int(input("Introduzca el denominador: "))
    
    return Simplificar_fraccion(numerador,denominador)

def Escribir_fraccion(numerador1,denominador1):
    return print(f"{numerador1}\n-\n{denominador1}")

def Calcular_mcd(numero1,numero2):
    return gcd(numero1,numero2)

def Simplificar_fraccion(numerador1,denominador1):
    mcd = Calcular_mcd(numerador1,denominador1)
    return int(numerador1/mcd), int(denominador1/mcd)

def Sumar_fracciones(numerador1,denominador1,numerador2,
                     denominador2):
    return Simplificar_fraccion((numerador1*denominador2+denominador1*numerador2),(denominador1*denominador2))

def Restar_fracciones(numerador1,denominador1,numerador2,denominador2):
    return Simplificar_fraccion((numerador1*denominador2-denominador1*numerador2),(denominador1*denominador2))

def Multiplicar_fracciones(numerador1,denominador1,numerador2,denominador2):
    return Simplificar_fraccion((numerador1*numerador2),(denominador1*denominador2))

def Dividir_fracciones(numerador1,denominador1,numerador2,denominador2):
    return Simplificar_fraccion((numerador1*denominador2),(denominador1*numerador2))

while True:
    print(f"#----- MENU ------#\n 1.-Sumar fracciones\n 2.-Restar fracciones\n 3.-Multiplicar fracciones\n 4.-Dividir fracciones\n 5.-Salir")
    opt = input("Introduzca la opción: ")
    if opt == "1":
        n1,d1=Leer_fraccion()
        n2,d2=Leer_fraccion()
        nsol,dsol=Sumar_fracciones(n1,d1,n2,d2)
        print("El resultado es:")
        Escribir_fraccion(nsol,dsol)
    elif opt == "2":
        n1,d1=Leer_fraccion()
        n2,d2=Leer_fraccion()
        nsol,dsol=Restar_fracciones(n1,d1,n2,d2)
        print("El resultado es:")
        Escribir_fraccion(nsol,dsol)
    elif opt == "3":
        n1,d1=Leer_fraccion()
        n2,d2=Leer_fraccion()
        nsol,dsol=Multiplicar_fracciones(n1,d1,n2,d2)
        print("El resultado es:")
        Escribir_fraccion(nsol,dsol)
    elif opt == "4":
        n1,d1=Leer_fraccion()
        n2,d2=Leer_fraccion()
        nsol,dsol=Dividir_fracciones(n1,d1,n2,d2)
        print("El resultado es:")
        Escribir_fraccion(nsol,dsol)
    elif opt == "5":
        break
    