#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa 
# negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa. 
# 1 tuuma = 2,54 cm

tuuma = float(input("Anna tuuma: "))

while tuuma > 0:

    tuuma_senttimetreinä = tuuma*2.54
    print("Antamasi tuuma on senttimetreinä:", tuuma_senttimetreinä)

    tuuma = input("Anna tuuma: ")