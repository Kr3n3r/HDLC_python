
class Persona():
    def __init__(self):
        self.nombre=str()
        self.edad=int()
        self.DNI=str()
    def setnombre(self,nombre):
        self.nombre = nombre
    def setedad(self,edad):
        self.edad=edad
    def setDNI(self,DNI):
        self.DNI=DNI
    def mostrar(self):
        return print(f'Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.DNI}')
    def esMayorDeEdad(self):
        if self.edad >= 18 :
            return True