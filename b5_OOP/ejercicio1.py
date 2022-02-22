# Realizar un programa que conste de una clase llamada Alumno que tenga como
# atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus
# atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha
# aprobado o no.

class Alumno:
    def __init__(self):
        self.nombre = str()
        self.nota = int()
        
    def setnombre(self,nombre):
        self.nombre = nombre
        
    def setnota(self,nota):
        self.nota = nota
        
    def printnota(self):
        return print(f"La nota es {self.nota}")
    
    def printnombre(self):
        return print(f"El nombre es {self.nombre}")
    
    def passed(self):
        if self.nota >= 5:
            return print(f"El alumno {self.nombre} ha aprobado")
        return print(f"El alumno {self.nombre} ha suspendido")
    
    def __del__(self):
        return print(f"El objeto ha sido destruido.")

AlejandroMarmolRomero = Alumno()
AlejandroMarmolRomero.setnombre("Alejandro Mármol Romero")
AlejandroMarmolRomero.setnota(6)
print(AlejandroMarmolRomero.passed())
AlejandroMarmolRomero = list()