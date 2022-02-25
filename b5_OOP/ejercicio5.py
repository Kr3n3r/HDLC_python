
class contacto():
    def __init__(self):
        self.nombre=''
        self.telefono=''
        self.email=''
    def getnombre(self):
        return self.nombre
    def gettelefono(self):
        return self.telefono
    def getemail(self):
        return self.email
    def setnombre(self,nombre):
        self.nombre=nombre
    def settelefono(self,telefono):
        self.telefono=telefono
    def setemail(self,email):
        self.email=email

class agenda():
    def __init__(self):
        self.contactos = list()
    def añadir_contacto(self,contacto):
        self.contactos.append(contacto)
    def lista_de_contactos(self):
        print(f"Los contactos son los siguientes:")
        for contacto in self.contactos:
            print(f"· {contacto.getnombre()}")
    def buscar_contacto(self,requiredcontacto):
        for contacto in self.contactos:
            if requiredcontacto in self.contacto.getnombre():
                print(f"· {contacto.getnombre()}")
    def editar_contacto(self,requiredcontacto):
        for contacto in self.contactos:
            if requiredcontacto == contacto.getnombre():
                contacto.setnombre(input('Introduce el nuevo nombre del contacto: '))
                contacto.settelefono(input('Introduce el nuevo teléfono del contacto: '))
                contacto.setemail(input('Introduce el nuevo email del contacto: '))
        return True
    def cerraragenda(self):
        print('La agenda ha sido destruida')
    # def __del__(self):
    #     print('La agenda ha sido destruida')

if __name__ == "__main__":
    agenda = agenda()
    contacto = contacto()
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
            contacto.setnombre(input('Introduce el nombre del nuevo contacto: '))
            contacto.settelefono(input('Introduce el teléfono del nuevo contacto: '))
            contacto.setemail(input('Introduce el email del nuevo contacto: '))
            agenda.añadir_contacto(contacto)
            print("Contacto creado correctamente")
        if opt == 2:
            agenda.lista_de_contactos()
        if opt == 3:
            break
        if opt == 4:
            break
        if opt == 5:
            agenda.cerraragenda()
            break