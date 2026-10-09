#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä

import random
luku = random.randint(1, 10)

arvaus = float(input("Arvaa luku: "))
while arvaus < luku:
    print("Liian pieni arvaus.")
    while arvaus > luku:
        print("Liian suuri arvaus.")
    if arvaus == luku:
        print("Oikein.")
    arvaus = float(input("Arvaa luku: "))