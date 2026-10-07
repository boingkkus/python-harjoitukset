kuukaudet = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
jarjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
vuodenaika = kuukaudet[jarjestysnumero - 1]
print(f"{jarjestysnumero}. vuodenaika on {vuodenaika}.")