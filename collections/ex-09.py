produkty = {
    "ziemniaki": 4.0,
    "kukurydza": 3.5,
    "pomidory": 6,
    "kapusta": 10
}

print("""Dostępne produkty:
- ziemniaki
- kukurydza
- pomidory
- kapusta""")

wartosc_koszyka = []
koszyk = {}

while True:
    nazwa = input("Podaj nazwę produktu lub 'koniec' aby przejść do kasy:")
    if nazwa == "koniec":
        print(f"Należność za zakupy: {sum(wartosc_koszyka)} PLN")
        print(f"Kupiłeś w sumie {len(koszyk)} produktów:", koszyk)
        break
    elif not nazwa in produkty:
        print("Produkt niedostępny.")
        continue
    ilosc = float(input("Podaj ilość:"))
    cena = produkty[nazwa] * ilosc
    wartosc_koszyka.append(cena)
    koszyk[nazwa] = ilosc
    print(f"Należność za {nazwa}: {cena} PLN")