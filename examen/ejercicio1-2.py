def mostrarProductos(nombres,precios):
    print(f'Productos:')
    for i in range(0,len(precios)):
        print(f'{nombres[i]}\t{precios[i]}€')
    return

def modificaPrecios(nombre,nombres,precios):
    for i in range(0,len(precios)):
        if nombres[i] == nombre:
            new_precio=5
            while new_precio >= 5:
                new_precio=input('Introduzca el nuevo precio: ')
                precios[i]=new_precio
                return
    print("El producto no ha podido ser localizado")
    return    

def modificaPieza(nombre,nombres):
    new_nombre = input("Introduce el nuevo nombre para el producto: ")
    if len(new_nombre) < 10:
        for i in range(0,len(nombres)):
            if nombres[i] == nombre:
                nombres[i] = new_nombre
    return

def actualizaPrecio(porcentaje,precios):
    if -100 <= porcentaje <= 100 :
        for i in range(0,len(precios)):
            precios[i]*=(1+porcentaje/100)

def main():
    from os import system
    nombres = ['barra','viena','pieza2',
               'pieza3','pieza4','pieza5']
    precios = [1,2,3,
               4,5,6]
    while True:
        print(f'----  MENU   -----')
        print(f'a)mostrarProductos')
        print(f'b)modificaPrecios')
        print(f'c)modificaPieza')
        print(f'd)actualizaPrecio')
        print(f'e)salir')
        opt = str(input('Introduce una de las opciones: '))
        if opt == 'a' :
            mostrarProductos(nombres,precios)
        if opt == 'b' :
            producto = input("Introduzca el nombre del producto: ")
            modificaPrecios(producto,nombres,precios)
        if opt == 'c' :
            for i in range(0,5):
                print(f'{i+1}. {nombres[i]}')
            opc = input("Introduzca el nombre del producto para cambiar su nombre: ")
            modificaPieza(opc,nombres)
        if opt == 'd' :
            porcentaje = input("Introduce un porcentaje: ")
            actualizaPrecio(float(porcentaje),precios)
        if opt == 'e' :
            break

main()