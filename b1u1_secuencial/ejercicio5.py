minutos = eval(input("Introduce el número de minutos para convertir a horas y minutos: "))
horas = minutos / 60
r_minutos = minutos%60
horas = int(horas)
print("Los minutos introducidos(",minutos,") equivalen a", horas," horas y ",r_minutos," minutos.")