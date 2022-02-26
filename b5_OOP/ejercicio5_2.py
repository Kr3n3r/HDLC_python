class Agenda():
    def __init__(self):
        self.contactos = []
    def añadir_contacto(self,nombre,telefono,email):
        self.contactos.append({'nombre' : nombre, 'telefono' : telefono, 'email' : email})
    def listar_contactos(self):
        print('Lista de contactos:')
        for contacto in self.contactos:
            print(f"·{contacto['nombre']} : {contacto['telefono']}, {contacto['email']}")
    def buscar_contacto(self,request):
        for contacto in self.contactos:
            if contacto['nombre'] == request or contacto['email'] == request or contacto['telefono'] == request:
                print(f"·{contacto['nombre']} : {contacto['telefono']}, {contacto['email']}")
    def editar_contacto(self,request):
        for contacto in self.contactos:
            if contacto['nombre'] == request:
                contacto['nombre'] = input('Introduce el nuevo nombre del contacto: ')
                contacto['telefono'] = input('Introduce el nuevo teléfono del contacto: ')
                contacto['email'] = input('Introduce el nuevo email del contacto: ')
                return True
        return False
    def cerrar_agenda(self):
        del self.contactos
        print(f'La agenda ha sido destruida.')

if __name__ == '__main__':
    agenda = Agenda()
    while True:
        print(f'-----   MENU    -----')
        print(f' 1.-Añadir contacto  ')
        print(f' 2.-Lista contactos  ')
        print(f' 3.-Buscar contacto  ')
        print(f' 4.-Editar contacto  ')
        print(f' 5.-Cerrar agenda    ')
        print(f'---------------------')
        opt = int(input('Elige una opción(1-5): '))
        if opt == 1:
            nombre = input('Introduce el nombre del nuevo contacto: ')
            telefono = input('Introduce el teléfono del nuevo contacto: ')
            email = input('Introduce el email del nuevo contacto: ')
            agenda.añadir_contacto(nombre, telefono, email)
            print('Contacto añadido!')
        if opt == 2:
            agenda.listar_contactos()
        if opt == 3:
            request = input('Introduce el nombre/telefono/email del contacto que quieres buscar: ')
            agenda.buscar_contacto(request)
        if opt == 4:
            request = input('Introduce el nombre del contacto que quieres editar: ')
            agenda.editar_contacto(request)
        if opt == 5:
            agenda.cerrar_agenda()
            break