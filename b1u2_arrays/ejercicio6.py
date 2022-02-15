# mostrar info de un mes
mes = ["","enero", "febrero", "marzo",
       "abril", "mayo", "junio",
       "julio", "agosto", "septiembre",
       "octubre", "noviembre", "diciembre"]
mes_dict = {
    "enero" : 31,
    "febrero" : 28,
    "marzo" : 31,
    "abril" : 30,
    "mayo" : 31,
    "junio" : 30,
    "julio" : 31,
    "agosto" : 31,
    "septiembre" : 30,
    "octubre" : 31,
    "noviembre" : 30,
    "diciembre" : 31
}

num_mes = int(input("Introduzca un número de mes: "))
print("El mes",mes[num_mes],"tiene",mes_dict[mes[num_mes]],"días ")