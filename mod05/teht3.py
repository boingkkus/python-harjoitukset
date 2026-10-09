#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luku = float(input("Anna luku: "))

while luku != "":
    luku = input("Anna luku: ")

    if luku < luku:
        print(luku)

else: 
    print(f"{luku}")