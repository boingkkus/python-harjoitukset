import random

def noppa():
    return random.randint(1,6)

heitto = 1
arvo = 0 

while arvo != 6:
    arvo = noppa()
    print(f"Heitto {heitto}: {arvo}")
    heitto = heitto + 1
