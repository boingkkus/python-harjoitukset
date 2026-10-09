#Tee luokka Kirja. Kirjalla on seuraavat ominaisuudet:
# nimi
# kirjoittaja
# sivumäärä
#Tee luokalle alustaja __init__. Tee lisäksi metodi:
#tulosta_tiedot()
#joka tulostaa kirjan tiedot. Luo ohjelmassa kaksi erilaista Kirja-oliota 
# ja tulosta molempien tiedot metodin avulla.

class Kirja():
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"Kirjan {self.nimi} on kirjoittanut {self.kirjoittaja}, ja siinä on {self.sivumäärä} sivua.")

kirja1 = Kirja("After the quake", "Haruki Murakami", 127)
kirja2 = Kirja("Cats", "Sagakuchi Kentaro", 143)

kirja1.tulosta_tiedot()
kirja2.tulosta_tiedot()