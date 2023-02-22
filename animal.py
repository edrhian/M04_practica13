'''
Atributs de animal
nom comú, nom cientific, longevitat, familia, grup i habitat
'''
class animal:
    def __init__(self, commonName, scientificName, longevity, family, group, habitat):
        self.commonName = commonName
        self.scientificName = scientificName
        self.longevity = longevity
        self.family = family
        self.group = group
        self.habitat = habitat

    #getters i setters
    def getCommonName(self):
        return self.commonName

    def setCommonName(self, commonName):
        self.commonName = commonName

    def getScientificName(self):
        return self.scientificName

    def setScientificName(self, scientificName):
        self.scientificName = scientificName

    def getLongevity(self):
        return self.longevity

    def setLongevity(self, longevity):
        self.longevity = longevity

    def getFamily(self):
        return self.family

    def setFamily(self, family):
        self.family = family

    def getGroup(self):
        return self.group

    def setGroup(self, group):
        self.group = group

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat
    #missatge
    def salutacio(self):
        print("El meu nom comú és {commonName}".format(commonName = self.commonName))
        print("El meu nom cientific és {scientificName}".format(scientificName=self.scientificName))
        print("Tinc una vida mitjana de {longevity} anys".format(longevity = self.longevity))
        print("Soc de la familia de {family}".format(family = self.family))
        print("Soc del grup de".format(group = self.group))
        print("El meu habitat esta en {habitat}".format(habitat = self.habitat))

