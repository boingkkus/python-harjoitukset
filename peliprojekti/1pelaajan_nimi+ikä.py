nimi = input("Mikä on nimesi?: ")
ikä = int(input("Mikä on ikäsi?: "))


if ikä >= 12 :
    print("Hei,", nimi, ikä,"v.")
    print("Tervetuloa pelaamaan peliä 'Pupen päivä'!")
else:
    print("Olet alaikäinen pelaamaan peliä.")


komento = input("Anna komento; jyrsi, kaiva, heitä, nuku tai lopeta: ")

while komento != "lopeta":
    if komento == "MAYDAY":
        break
    print("Suoritan toiminnon: " + komento)
    if komento == "jyrsi":
        print("Etsit huoneesta maukkaan näköisen laturin ja alat mautustelemaan sitä. Sähköinen heinä on harvinainen herkku.")
    if komento == "kaiva":
        print("Änget itsesi sängyn alle kauimpaan nurkkaan ja alat kaivamaan lattiaa muristen. 'Tänään alakerran naapurit saavat tuntea vihani.'")
    if komento == "heitä":
        print("Näet irtotavaran lattialla ja päätät tänään olevan sen viimeinen päivä. Noukit sen nököhampaittesi väliin ja viskaiset sen niin kovaa kuin kykenet. 'Pois minun lattialtani!'")
    if komento == "nuku":
        print("Suuntaat sukkalaatikon viereen nokosille huoneen nurkkaan. Vielä ei ole aika aamulle.")
    komento = input("Anna komento; jyrsi, kaiva, heitä, nuku tai lopeta: ")
else:
    print("Näkemiin, tervetuloa pelaamaan uudestaan!")
print("Toiminnot lopetettu. ")