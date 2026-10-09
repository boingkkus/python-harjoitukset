#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.


luvut = []

anna_luku = input("Anna luku tai lopeta painamalla enter: ")

while anna_luku != "":
    luvutt = int(anna_luku)
    luvut.append(luvutt)
    anna_luku = input("Anna luku: ")
    
luvut.sort(reverse = True)

for luku in luvut:
    print(luku)