def analizuj_imie(imie):
    if imie.endswith('a'):
        print("kobieta")
    else:
        print("mężczyzna")
    print(len(imie), imie.endswith('a'))

imie = input("Podaj imie:")
analizuj_imie(imie)