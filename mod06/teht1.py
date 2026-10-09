#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
#Käytä for-toistorakennetta.

import random

noppien_silmäluvut = []

arpakuutioiden_lukumäärä = int(input("Anna arpakuutioiden lukumäärä: "))


for silmäluku in range(arpakuutioiden_lukumäärä):
    silmäluku = random.randint(1,6)
    noppien_silmäluvut.append(silmäluku)
    
summa = sum(noppien_silmäluvut)
print(summa)