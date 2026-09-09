nimi = input("Mikä on nimesi?: ")
ikä = int(input("Mikä on ikäsi?: "))


if ikä >= 12 :
    print("Hei,", nimi, ikä,"v.")
    print("Tervetuloa pelaamaan peliä 'Pupen päivä'!")
else:
    print("Olet alaikäinen pelaamaan peliä.")


komento = input("Anna komento; jyrsi, kaiva, heitä, nuku, katso pussukkaan tai lopeta: ")

while komento != "lopeta":
    if komento == "MAYDAY":
        break
    print("Suoritan toiminnon: " + komento)
    if komento == "jyrsi":
        print("Etsit huoneesta maukkaan näköisen laturin ja alat mutustelemaan sitä. Sähköinen heinä on harvinainen herkku.")
    if komento == "kaiva":
        print("Änget itsesi sängyn alle kauimpaan nurkkaan ja alat kaivamaan lattiaa muristen. 'Tänään alakerran naapurit saavat tuntea vihani.'")
    if komento == "nuku":
        print("Suuntaat sukkalaatikon viereen nokosille huoneen nurkkaan. Vielä ei ole aika aamulle.")
    if komento == "heitä":
        print("Näet juomakupin lattialla ja päätät tänään olevan sen viimeinen päivä. Noukit sen nököhampaittesi väliin ja viskaiset sen niin kovaa kuin kykenet. 'Pois minun lattialtani!'")
        vastaus = input("Lisätäänkö juomakuppi pussukkaan? y/n:")
        if vastaus == "y":
            def inventaario(tavarat):
                return
            pussukka = ["Porkkana", "Laturin pala", "Papana?"]
            pussukka.append("juomakuppi")
            inventaario(pussukka)
    if komento == "katso pussukkaan":
        def inventaario(tavarat):
            print("Katsotaan mitä pussukasta löytyy: ")
            for t in tavarat:
                print("- " + t)
            return
        pussukka = ["Porkkana", "Laturin pala", "Papana?"]
        inventaario(pussukka)
        

       
    komento = input("Anna komento; jyrsi, kaiva, heitä, nuku, katso pussukkaan tai lopeta: ")
else:
    print("Näkemiin, tervetuloa pelaamaan uudestaan!")
print("Toiminnot lopetettu. ")