def czy_jest_pierwsza(liczba):
    liczba = int(liczba)
    if liczba <= 1:
        return False
    for mianownik in range(2, liczba):
        if liczba % mianownik == 0:
            return False
    return True
liczba = input("Wpisz liczbę:")
print(f"{liczba} jest liczbą pierwszą?", czy_jest_pierwsza(liczba))
