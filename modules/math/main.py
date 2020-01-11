from mathematica.algebra import matrices
from mathematica.geometry import figures

operacja = input("Chcesz zająć się (a)lgebrą czy (g)eometrią? ")
if operacja == "g":
    bok = float(input("Podaj wymiar a "))
    wysokosc = float(input("Podaj wymiar h "))
    print(f"""Powierzchnia kwadratu {figures.square_area(bok)}
Powierzchnia trójkąta {figures.triangle_area(bok, wysokosc)}""")
if operacja == "a":
    matryca1 = input("Wpisz pierwszą matrycę ")
    matryca1 = matryca1.split()
    matryca1 = list(map(int, matryca1))
    matryca2 = input("Wpisz drugą matrycę ")
    matryca2 = matryca2.split()
    matryca2 = list(map(int, matryca2))
    print(f"""Suma list {matrices.add_matrices(matryca1, matryca2)}
Różnica list {matrices.sub_matrices(matryca1, matryca2)}""")