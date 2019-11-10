szerokosc = float(input("Podaj szerokość w cm: "))
glebokosc = float(input("Podaj glebokość w cm: "))
wysokosc = float(input("Podaj wysokość w cm: "))
pojemnosc_karton = szerokosc * glebokosc * wysokosc
print(f"Pojemność kartonu wynosi {round(pojemnosc_karton, 2)} cm3, pojemność jest większa od 1 litra: {pojemnosc_karton / 1000 > 1}.")
if pojemnosc_karton / 1000 <= 1.0:
    print("Znajdź większy karton!")
else:
    print("Pakuj śmiało :-)")