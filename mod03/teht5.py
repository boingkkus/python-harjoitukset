leiviskä_str = input("Anna leivisköjen määrä: ")
naula_str = input("Anna naulojen määrä: ")
luoti_str = input("Anna luotien määrä: ")
leiviskä = float(leiviskä_str)
naula = float(naula_str)
luoti = float(luoti_str)
naula = leiviskä * 20
luoti = naula * 32
gramma = luoti * 13.3
kilogramma = int(gramma // 1000)
gramma = round(gramma % 1000, 2)
print("Massa nykymittojen mukaan: "),print(kilogramma," kilogrammaa"),print(gramma," grammaa")