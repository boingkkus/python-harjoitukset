class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeudenmuutos):
        uusi_nopeus = self.nopeus_nyt + nopeudenmuutos
        if uusi_nopeus < 0:
            uusi_nopeus = 0
        elif uusi_nopeus > self.huippunopeus:
            uusi_nopeus = self.huippunopeus
        self.nopeus_nyt = uusi_nopeus

    def kulje(self, tunti):
        kuljettu_matka = self.kuljettu_matka + self.nopeus_nyt * tunti
        self.kuljettu_matka = kuljettu_matka


auto = Auto("ABC_123", 142)

print(f"Uuden auton rekisteritunnus on {auto.rekisteritunnus} ja huippunopeus on {auto.huippunopeus}km/h.")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

auto.kulje(1.5)

print(f"Auton nopeus nyt: {auto.nopeus_nyt}km/h")

print(f"Auton kuljettu matka on {auto.kuljettu_matka}km")

auto.kiihdytä(-200)

print(f"Auton nopeus nyt: {auto.nopeus_nyt}km/h")