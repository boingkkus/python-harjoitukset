#Tee luokka Opiskelija. Opiskelijalla on nimi ja pistemäärä.
#Luo vähintään kolme opiskelijaoliota ja tallenna ne listaan. 
#Käy lista läpi silmukan avulla ja tulosta jokaisenopiskelijan nimi ja pistemäärä.

class Opiskelija():

    def __init__(self, nimi, pistemäärä):
        self.nimi = nimi
        self.pistemäärä = pistemäärä

opiskelijat = []
opiskelija1 = Opiskelija("tiia", 55)
opiskelija2 = Opiskelija("mette", 67)
opiskelija3 = Opiskelija("Puppe", 32)

opiskelijat.append(opiskelija1)
opiskelijat.append(opiskelija2)
opiskelijat.append(opiskelija3)

for opiskelija in opiskelijat:
    if opiskelija.pistemäärä >= 50:
        print(f"Opiskelijat ja pistemäärät ovat: {opiskelija.nimi} {opiskelija.pistemäärä}")