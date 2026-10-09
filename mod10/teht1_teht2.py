class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_määrä = hissien_määrä
        self.hissit = []

        for hissi in range(hissien_määrä):
            hissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissinumero, kohdekerros):
        hissi = self.hissit[hissinumero-1]
        self.kohdekerros = kohdekerros
        hissi.siirry_kerrokseen(kohdekerros)



class Hissi():
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")

    def kerros_ylös(self):
         if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")

    def siirry_kerrokseen(self, siirry):
        while self.nykyinen_kerros < siirry:
            self.kerros_ylös()
        while self.nykyinen_kerros > siirry:
            self.kerros_alas()

talo = Talo(1, 5, 2)

talo.aja_hissiä(1, 3)
talo.aja_hissiä(1, 2)
talo.aja_hissiä(1, 5)

talo.aja_hissiä(2, 3)
talo.aja_hissiä(2, 1)