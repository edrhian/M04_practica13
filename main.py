from animal import animal
from vehicle import vehicle
from school import school
from book import book
from user import user
from university import university



#Integrant A Edrhian Valerio
capybara = animal("Capybara", "Hydrocoreus", 45, "Caviidae", "Mamifer", "Sudafrica")
pingüi = animal("Pingüi", "Spheniscieade", 30, "Spheniscieade", "Au", "Pol Sur")

capybara.salutacio()
pingüi.salutacio()

print("----------------------")

toyotaCorola = vehicle("Diesel", "Toyota", "Blanc", "Japo", "2727 HGY", 139)
volkswagenCaddy = vehicle("Diesel", "Volkswagen", "Blau", "Alemanya", "3059 POO", 158)

toyotaCorola.parts()
volkswagenCaddy.parts()

print("----------------------")

carlit = school("Escola Carlit", 3, 40, 3000, 1, 9)
balmes = school("Escola Balmes", 4, 60, 5000, 2, 15)

carlit.info()
balmes.info()
#Canvi d'atributs
print("----------------------")
print("Canvi d'atributs")
print("----------------------")
capybara.setHabitat("Rusia")
pingüi.setLongevity(43)

capybara.salutacio()
pingüi.salutacio()
print("----------------------")

toyotaCorola.setColor("Negre")
volkswagenCaddy.setCountry("Espanya")

toyotaCorola.parts()
volkswagenCaddy.parts()

print("----------------------")
carlit.setNFloors(1)
balmes.setNClassrooms(200)

carlit.info()
balmes.info()

#Integrant b Mustapha Bouleili
elLaberinto = book("El laberinto", "dur", 300, "Marcos", "11-11-2011", 20)
shadow= book("Shadow", "dur", 878, "Mark", "11-11-2015", 15)
elLaberinto.info()
shadow.info()

print("----------------------")

juan = user("Juan", "Garcia", 22, "25342393X", "jgarcia@gmail.com", "673234987")
alberto = user("Alberto", "Garcia", 27, "25341873Z", "agarcia@gmail.com", "673234467")
juan.salutacio()
alberto.salutacio()

print("----------------------")

uab = university("UAB", "Arago, 133", 15, 200, 8, 100)
upc = university("UPC", "Arago, 180", 14, 150, 6, 80)
uab.info()
upc.info()

#canvis
elLaberinto.setNpage(676)
shadow.setPrice(33)
print("----------------------")
juan.setAage(21)
alberto.setName("Alfredo")
print("----------------------")
uab.setArea(500)
upc.setNClass(154)