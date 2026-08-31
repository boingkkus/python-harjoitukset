kuha = int(input("Anna kuhan pituus (cm): "))

alamittainen = 37 - kuha

if kuha <= 37:
    print("Laske kuha takaisin järveen.")
    print("Alimmasta sallitusta pyyntimitasta puuttuu; ")
    print(alamittainen, "cm.")
else:
    print("Kiva kuha.")