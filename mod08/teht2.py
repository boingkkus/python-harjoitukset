nimet = set()

nimi = input("Anna uusi nimi tai paina enter: ")

while nimet != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
        print("Uusi nimi")
    nimi = input("Anna nimi: ")

    for n in nimet:
        print(n)