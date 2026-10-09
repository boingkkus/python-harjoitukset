# 1. luodaan monikko, joka sisältää kolmen kaupungin nimet
# 2. luodaan joukko, johon lisätään viisi lukua, joista osa on samoja
# 3. luodaan sanakirja, johon tallennetaan opiskelijan nimi, opiskelijanumero ja ryhmä
# Tulosta kaikki kolme tietorakennetta

kaupungit = ("Roma", "Como", "Seoul")

luvut = set()
luvut.add("5")
luvut.add("33")
luvut.add("55")
luvut.add("55")
luvut.add("33")
luvut.remove("5")

opiskelijatiedot = {"nimi": "puppe",
                    "opiskelijanumero": 5543}
opiskelijatiedot["ryhmä"] = "23B"

print(kaupungit, luvut, opiskelijatiedot)