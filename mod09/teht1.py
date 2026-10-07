class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0

auto = Auto("ABC_123", 142)

print(f"Uuden auton rekisteritunnus on {auto.rekisteritunnus} ja huippunopeus on {auto.huippunopeus}km/h.")