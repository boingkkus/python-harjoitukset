class Huone():
    def __init__(self, nimi: str):
        self.nimi = self.huoneet
        self.esineet = ['papana']

    def pudota_esine_huoneeseen(self, esine):
        self.esineet.append(esine)
    #tavallaan näitä ei tarvii, koska papanoiden määrä on loputon. mut idk ei ainakaan tota^ alempi on ihan hyvä
    def kerää_esine_huoneesta(self, esine):
         if esine in self.esineet:
              self.esineet.remove(esine)

    def huoneet(self, makuuhuone, olohuone, eteinen):
        makuuhuone = Huone("Makuuhuone")
        olohuone = Huone("Olohuone")
        eteinen = Huone("Eteinen")

class Pelaaja():
    def __init__(self, nimi, ikä, sijainti ='makuuhuone'):
        self.nimi = nimi
        self.ikä = ikä
        self.esineet = ['papana']
        self.sijainti = sijainti

    def luettele_esine(self):
        return self.esineet

    def liiku(self, sijainti):    
        print(f"{self.nimi}, 'liikkuu huoneeseen: ', {self.Huone.sijainti},'.'")
        return

    def kerää_esine(self):
        if self.sijainti.esineet:
            kerätty = self.sijainti.esineet[0]
            self.sijainti.kerää_esine(kerätty)
            self.esineet.append(kerätty)
            print(f"{self.nimi}, 'kerää esineen: ', {self.esine},'.'")
            return

class Esine():
    def __init__(self, nimi: str):
        self.nimi = nimi

def __str__(self):
    return (f"{self.nimi}")


with open("peliprojekti/intro.txt") as tiedosto:
    data = tiedosto.read()
    print(data)

with open("peliprojekti/ohjeet.txt") as tiedosto:
    data = tiedosto.read()
    print(data)

#nää vähänniiku esimerkkeinä, en tiiä mitä mun pitäis tänne tallentaa
#with open("peliprojekti/save.txt", "w") as tiedosto:
#    tiedosto.write("Pelaaja pääsi tasolle 2.")

#with open("peliprojekti/save.txt", "a") as tiedosto:
#    tiedosto.write("Pelaaja pääsi tasolle 3.\n")
#    tiedosto.write("Pelaaja pääsi tasolle 4.\n")
    #pitääks tännekki laittaa niitä vitun olioita tai funktioita idfk
    #en tiiä tarviinko näitä ees lowkey ?

#with open("peliprojekti/save.txt", "r") as tiedosto:
#    data = tiedosto.read()
#    print(data)




def tallenna(Pelaaja):
    import json

    tallennus_data = {
        "nimi": Pelaaja.nimi,
        'ikä': Pelaaja.ikä,
        "esineet": Pelaaja.esineet [''],
        "sijainti": Pelaaja.sijainti
    }
    with open("peliprojekti/save.json", "w") as tiedosto:
        json.dump(tallennus_data, tiedosto)
    with open("peliprojekti/save.json", "r") as tiedosto:
        data_luettu = json.load(tiedosto)
    print(f"Pelaaja: {data_luettu['pelaaja']}, taso: {data_luettu['ikä']}, esineet: {data_luettu['esineet']}, sijainti: {data_luettu['sijainti']}")



nimi = input("Mikä on nimesi?: ")
ikä = int(input("Mikä on ikäsi?: "))


if ikä >= 12 :
    print("Hei,", nimi, ikä,"v." )
    print("Tervetuloa pelaamaan peliä 'Pupun päivä'!" )

    #pelin päävalikko
    komento1 = input("Päävalikko; Aloita peli tai lopeta: ")

    if komento1 != "lopeta":
        print("Aloitetaan peli Pupun Päivä!")
    if komento1 == 'lopeta':
        quit()

    #pelin aloitustekstit
    print("Heräät makoisilta päiväunilta makuuhuoneesta, ja huomaat olevasi ihan yksin.")
    print("Katselet ympärillesi ja mietit, 'missä rakas ystäväni Myy oikein on? En voi elää ilman sitä täydellisyyttä. Minun täytyy etsiä hänet.'"
          )

    #ensimmäisessä huoneessa olo / sieltä lähteminen
    komento = input("Anna komento; syö heinää, nuku lisää, katso pussukkaan, katso ympärillesi poistu makuuhuoneesta tai lopeta: ")

    while komento != "lopeta":
        if komento == "LOPETA":
            break

        print("Suoritan toiminnon: " + komento)

        if komento == "syö heinää":
            print("Pompit heinäkasan luokse ja alat jyrsimään. 'Tarvitsen energiaa Myyn löytämiseen.'")
            print("Voimasi kasvavat ja lähdet etsimään Myytä, saatuasi heinästä lisää energiaa.\n")

        if komento == "nuku lisää":
            print("Suuntaat sukkalaatikon viereen huoneen nurkkaan jatkamaan unia. 'Vielä ei ole aika aamulle.'")
            print("Heräät tunnin päästä uudelleen, valmiina Myyn etsintään.\n")
        
        if komento == "katso ympärillesi":
            print("'Hmm. En näe Myytä. Mihin Myy on voinut mennä?'") 
            print("Myyn sijaan näet kasan papanoita lattialla. 'Ovatkohan nämä Myyn?'\n")

            vastaus = input("Lisätäänkö papana pussukkaan? y/n:")

            if vastaus == "y":
                print("'Ehkä tämä voi tulla hyödylliseksi etsiessäni Myytä.'\n")
                Pelaaja.kerää_esine #tää myös
                #esine 'papana' lisättiin pussukkaan tms ?

            if vastaus == "n":
                print("'Hmm. Ehkä papana on parempi jättää siihen. Äiti pitää niistä tuossa kovasti.'\n")

        if komento == "katso pussukkaan":
            print("Katsotaan mitä pussukasta löytyy: \n")
            #for p in Pelaaja.luettele_esine('self'):
            #    print("- " + p)

        if komento == "poistu makuuhuoneesta":
            print("Suuntaat makuuhuoneen ovesta ulos uutta maailmaa kohti.\n") 

            komento2 = input("Anna komento suuntaa...; makuuhuoneeseen, olohuoneeseen, eteiseen, tai lopeta: ")

            while komento2 != "lopeta":
                if komento2 == "LOPETA":
                    break

                if komento2 == "olohuoneeseen":
                    print("'Myy tykkää viettää paljon aikaa olohuoneessa... katson jos hän löytyisi sieltä.'\n")
                    
                    komento3 = input("Anna komento; katso ympärillesi, katso pussukkaan, mene syvemmälle, tai lopeta: ")

                    while komento3 != "lopeta":
                        if komento3 == "LOPETA":
                            break

                        if komento3 == "katso ympärillesi":
                            print("Näet lattialla olevan paljon papanoita. 'Onkohan Myy tehnyt nuo?'\n")
                            
                            vastaus2 = input("Lisätäänkö papana pussukkaan? y/n:")
                            
                            if vastaus2 == "y":
                                print("'Ehkä tämä voi tulla hyödylliseksi etsiessäni Myytä.'\n")
                                Pelaaja.kerää_esine #tää myös
                            
                            if vastaus2 == "n":
                                print("'Hmm. Ehkä papana on parempi jättää siihen. Äiti pitää niistä tuossa kovasti.'\n")

                        if komento3 == "katso pussukkaan":
                            print("Katsotaan mitä pussukasta löytyy: \n")
                            #for p in Pelaaja.esineet:
                            #    print("- " + p)
                            #tähän korjataan se pussukka koodi :DDD

                        if komento3 == "mene syvemmälle":    
                            print("Menet syvemmälle olohuoneeseen ja alat kuulla pientä rapinaa. 'Onkohan tuo Myy?!'")
                            print("Suuntaat katseesi heiluvaan heinämökkiin. 'Hui, pelottavaa. Eihän Myy vain olisi tuolla?'\n")
                            
                            mökkeys = input("Menetkö heinämökkiä kohti? y/n: ")
                            if mökkeys == "y":
                                print("Lähestyt kovasti heiluvaa heinämökkiä.") 
                                print("Mökki heiluu niin kovasti, että se näyttää siltä, kuin sen sisällä olisi suuri peto.\n")
                                
                                mökkeys = input("Menetkö heinämökkiä kohti? y/n: ")
                                if mökkeys == "y":
                                    print("Lähestyt pelottavaa mökkiä ja näet suuren, kirkkaan valkoisen valon, joka vain kasvaa lähestyessäsi hurjasti heiluvaa mökkiä. ")
                                    print("'Mikä on tämä valo...? Se lähes sokaisee minut kirkkaudellaan... Tunnen jonkin suuren läsnäolon mökissä... Se on varmasti Myy!'\n")
                                    
                                    kurkkaus = input("Kurkkaatko mökkiin? y/n: ")
                                    if kurkkaus == "y":
                                        print("Kurkkaat varovasti mökkiin ja näät maailman kauneimman ilmestyksen edessäsi. " \
                                        "'MYY! Olen etsinyt sinua kaikkialta!'")
                                        print("Myy vilkaisee sinuun päin heinänkorsi suupielestään roikkuen, ja tunnet valaistumisen. Koko vartalosi rentoutuu ja tunnet suurta rauhaa ja onnellisuutta.")
                                        print("'Tästä elämässä on kyse. Rakas Myyni on viimein löytynyt. Olen löytänyt rauhan ja tarkoituksen tyhjästä olemassaolostani. " \
                                        "Vastaus oli aina Myy. Vastaus tulee aina olemaan Myy.'\n")

                                        print("Pääsit pelin loppuun! Löysit Myyn, eli elämän tarkoituksen, ja valaistuit! Onnittelut. ")
                                        #if Pelaaja.esineet == ["papana", "papana", "papana"]:
                                        #    print("Löysit ja keräsit myös kaikki papanat matkallasi Myyn luokse! Läpäisit pelin! Onnittelut!")
                                        quit()

                            if mökkeys == "n":
                                print("Menikö pupulla pupu pöksyyn?")

                        komento3 = input("Anna komento; katso ympärillesi, katso pussukkaan, mene syvemmälle, tai lopeta: ")

                if komento2 == "makuuhuoneeseen":
                    #se vitun sijaintikoodi
                    print("'Makuuhuone vaikutti turvalliselta paikalta. Ehkä Myy palaa itse takaisin sinne...'")
                    print("Miten kehtaat jättää Myyn etsinnän kesken. Myy on ainoa tärkeä asia tässä maailmassa. Kuole saasta.")
                    print("Sait salamasta iskun suoraan päähän. Et voi todistaa Myyn tehneen tätä.")
                    quit()

                if komento2 == "eteiseen":
                    #tähän se vitun sijainti koodi
                    print("'En ole koskaan käynyt täällä ennen... eikä tänäänkään ole se päivä. Kynnys on ihan liian hurja... eihän täällä edes näy papanoita...'\n")
                    
                    mennäänkö_eteiseen = input("Yritetäänkö eteiseen menoa uudestaan? y/n: ")
                    if mennäänkö_eteiseen == "y":
                        print("Eteisen kynnys oli liian korkea pienelle pupulle. Kompastut ja lyöt pikku nenusi. Myytä ei voi löytää tässä kunnossa...")
                        quit()
                    if mennäänkö_eteiseen == "n":
                        print("'Ehkä näin on turvallisinta. Omaan intuitioon tulee luottaa. Tuskinpa Myy olisi eteiseen mennyt...'\n")

                komento2 = input("Anna komento suuntaa...; makuuhuoneeseen, olohuoneeseen, eteiseen, tai lopeta: ")

        komento = input("Anna komento; syö heinää, nuku lisää, katso pussukkaan, katso ympärillesi poistu makuuhuoneesta tai lopeta: ")
    
    else: 
        print("Näkemiin, tervetuloa pelaamaan uudestaan!")
    print("Toiminnot lopetettu. ")

else:
    print("Olet alaikäinen pelaamaan peliä.")
    print("Peli sammutetaan.")