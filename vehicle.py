'''
Atributs de vehicle
tipus de motor, color, pais, placa de llicencia, cavalls vapor
'''
class vehicle:
    def __init__(self, motorType, brand, color, country, licensePlate, horsePower):
        self.motorType = motorType
        self.brand = brand
        self.color = color
        self.country = country
        self.licensePlate = licensePlate
        self.horsePower = horsePower

    # getters i setters
    def getMotorType(self):
        return self.motorType

    def setMotorType(self, motorType):
        self.motorType = motorType

    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getCountry(self):
        return self.country

    def setCountry(self, country):
        self.country = country

    def getLicensePlate(self):
        return self.licensePlate

    def setLicensePlate(self, licensePlate):
        self.licensePlate = licensePlate

    def getHorsePower(self):
        return self.horsePower

    def setHorsePower(self, horsePower):
        self.horsePower = horsePower
    #Missatge
    def parts(self):
        print("Tipus de motor: {motorType}".format(motorType=self.motorType))
        print("Marca del vehicle: {brand}".format(brand=self.brand))
        print("Color del vehicle: {color}".format(color=self.color))
        print("País: {country}".format(country=self.country))
        print("Número de placa: {licensePlate}".format(licensePlate=self.licensePlate))
        print("Cavalls Vapor (CV): {horsePower}".format(horsePower=self.horsePower))

