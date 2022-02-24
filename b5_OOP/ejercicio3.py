
class triangle():
    def __init__(self):
        self.side=[0,0,0]
    def setside(self, side1, side2,side3):
        self.side=[side1,side2,side3]
    def getside(self):
        return self.side
    def getHigherSide(self):
        return self.side.max()
    def type(self):
        sorted = list(self.getside())
        if sorted[0] == sorted[1] & sorted[1] == sorted[2]:
            return "Es equilátero"
        if sorted[0] == sorted[1] | sorted[1] == sorted[2]:
            return "Es isósceles"
        return "Es escaleno"
            

triangulo = triangle()
triangulo.setside(2,5,5)
print(triangulo.type())