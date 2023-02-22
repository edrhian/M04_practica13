"""Els atributs de la classe university són:
 el nom, la direcció, els graus, l'area, el numero de plantas i classes"""
class university:
    def __init__(self, name, direction, degree, area, nFloors, nClass):
        self.name = name
        self.direction = direction
        self.degree = degree
        self.area = area
        self.nFloors = nFloors
        self.nClass = nClass

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getDirection(self):
        return self.direction
    def setDirection(self, direction):
        self.direction = direction
    def getDegree(self):
        return self.degree
    def setDegree(self, degree):
        self.degree = degree
    def getArea(self):
        return self.area
    def setArea(self, area):
        self.area = area
    def getNFloors(self):
        return self.nFloors
    def setNFloors(self, nFloors):
        self.nFloors = nFloors
    def getNClass(self):
        return self.nClass
    def setNClass(self, nClass):
        self.nClass = nClass

    def info(self):
        print("El nom de la universitat és {name}".format(name=self.name))
        print("És troba en el carrer {direction}".format(direction=self.direction))
        print("Té {degree} graus".format(degree=self.degree))
        print("L'area es de {area} m2".format(area=self.area))
        print("Té {nFloors} plantes".format(nFloors=self.nFloors))
        print("Té {nClass} aules".format(nClass=self.nClass))



