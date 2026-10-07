def gallon(num):
    litra = num * 3.785
    return litra

num = int(input("Syötä gallonamäärä: "))

while num >= 0:
    print(f"{num} gallonaa on {gallon(num)} litraa")
    num = int(input("Syötä seuraava gallonamäärä: "))
