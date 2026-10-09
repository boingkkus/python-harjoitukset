class Auto:
 def __init__(self, merkki, vuosimalli):
    self.merkki = merkki
    self.vuosimalli = vuosimalli

auto = Auto("Toyota", 2020)
print(f"{auto.merkki}, {auto.vuosimalli}")