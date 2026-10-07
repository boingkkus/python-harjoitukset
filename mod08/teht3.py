lentoasematiedot = {"EFHK": "Helsinki", "RJTT": "Tokyo", "RJOO": "Osaka", "RKSI": "Seoul", "RKPP": "Busan", "RKPC": "Jeju", }
toiminto = input("Haluatko syöttää uuden lentoaseman (syötä), hakea jo syötetyn lentoaseman tiedot (hae) vai lopettaa? (lopeta): ")

while toiminto != "lopeta":
    if toiminto == "syötä":
        lentoaseman_nimi = input("Anna lentoaseman nimi: ")
        ICAO = input("Anna lentoaseman ICAO-koodi: ")
        lentoasematiedot[ICAO] = lentoaseman_nimi
    elif toiminto == "hae":
        hae = input("Anna lentoaseman ICAO-koodi: ")
        if hae in lentoasematiedot: 
            print(lentoasematiedot[hae])
    toiminto = input("Haluatko syöttää uuden lentoaseman (syötä), hakea jo syötetyn lentoaseman tiedot (hae) vai lopettaa? (lopeta): ")