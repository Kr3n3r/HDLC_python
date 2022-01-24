# Suponiendo que hemos introducido una cadena por teclado que
# representa una frase (palabras separadas por espacios), realiza un programa
# que cuente cuantas palabras tiene
frase = input("Introduce una frase para contar cuantas palabras tiene: ")
frase = frase.split()
print("Tiene",frase.__len__(),"palabras.")