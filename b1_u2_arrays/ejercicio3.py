# lee 5 notas, muestra mayor, menor y media
# import stadistics
notas = []
while notas.__len__() != 5:
    nota=eval(input("Introduce una nota: "))
    notas.append(nota)
print("La nota mayor es:",max(notas))
print("La menor de las notas es:",min(notas))
print("La media de las notas es:",(sum(notas)/len(notas)))