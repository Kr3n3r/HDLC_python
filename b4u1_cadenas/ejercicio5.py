# Si tenemos una cadena con un nombre y apellidos,
# realizar un programa 
# que muestre las iniciales en mayúsculas.
nombrecompleto = "alejandro marmol romero"
nombre=str()
for element in nombrecompleto.split():
    nombre+=element.capitalize()+" "
print(nombre)