import random

def noppa(max):
    num = random.randint(1,max)
    return num

heitto = 1
arvo = 0
max = int(input("Syötä määrä: "))
while arvo != max:
    arvo = noppa(max)
    print(arvo)