# Pide una cadena y dos caracteres por teclado 
# (valida que sea un carácter),
# sustituye la aparición del primer carácter 
# en la cadena por el segundo
# carácter
cadena = input("Introduce una cadena de caracteres: ")
while True:
    char1 = input("Introduce un primer caracter: ")
    char2 = input("Introduce un segundo caracter: ")
    if char1.__len__()!=1 and char2.__len__()!=1:
        print("Debes introducir un solo caracter.")
    else:
        break

print(cadena.replace(char1, char2))