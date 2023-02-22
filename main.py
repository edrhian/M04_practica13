from animal import animal
from vehicle import vehicle
from school import school




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