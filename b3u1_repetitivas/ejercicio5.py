#comprueba si es vocal o no
vocal = set("aeiou")
lst=("a","e","i","o","u")
while True:
    string=input("Introduce un caracter: ")
    if string.lower() in vocal:
        print("VOCAL")
    elif string == " ":
        break
    else:
        print("No vocal")
print("Ejecución terminada")