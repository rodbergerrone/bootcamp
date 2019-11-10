miastoA = input("Podaj nazwę miasta startowego: ")
miastoB = input("Poaaj nazwę miasta końcowego: ")
dystans = input(f"Podaj dystans pomiędzy {miastoA}-{miastoB}: ")
cena_paliwa = input("Podaj cenę paliwa: ")
spalanie = input("Ile spala twoje auto na 100km: ")
print(f"Koszt przejazdu z {miastoA} do {miastoB} wynosi:", int(float(dystans) / 100 * float(cena_paliwa) * float(spalanie)), "PLN")

#koszt = float(dystans) / 100 * float(cena_paliwa) * float(spalanie)
#print(f"Koszt przejazdu z {miastoA} do {miastoB} wynosi {int(koszt)} PLN")