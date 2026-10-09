class Henkilo:
 
 def __init__(self, nimi):
    self.nimi = nimi
 
 def esittele(self):
    print("Olen", self.nimi)

class Opiskelija(Henkilo):
     pass

opiskelija = Opiskelija("Anna")

opiskelija.esittele()