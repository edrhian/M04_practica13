"""Els atributs de la classe user són:
 el nom, el cognom, l'edat, el dni, el mail i el numero de telefon"""
class user:
    def __init__(self, name, surname, age, dni, mail, number):
        self.name = name
        self.surname = surname
        self.age = age
        self.dni = dni
        self.mail = mail
        self.number = number

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSurname(self):
        return self.surname

    def setSurname(self, surname):
        self.surname = surname

    def getAge(self):
        return self.age

    def setAage(self, age):
        self.age = age

    def getDni(self):
        return self.dni

    def setDni(self, dni):
        self.dni = dni

    def getMail(self):
        return self.mail

    def setMail(self, mail):
        self.mail = mail

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def salutacio(self):
        print("El usuari és diu {name}".format(name=self.name))
        print("El seu cognom és {surname}".format(surname=self.surname))
        print("Té {age} anys".format(age=self.age))
        print("El seu dni és {dni}".format(dni=self.dni))
        print("El seu correu electronic és {mail}".format(mail=self.mail))
        print("El seu numero de telèfon és {number}".format(number=self.number))