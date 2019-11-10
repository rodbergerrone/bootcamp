liczba_min = None
liczba_max = None

while True:
    dane = input("Wpisz liczbę lub 'koniec': ")
    if dane.lower() == "koniec":
        break
    if dane == "":
        print("Nic nie wpisałeś!")
        continue
    if dane.isdecimal() == False: # Trzeba dodać wyjątek bo wyrzuca minusowe liczby jako niedozwolony znak.
        print("Wpisałeś niedozwolony znak!")
        continue
    liczba = int(dane)
    if liczba_min == None or liczba < liczba_min:
        liczba_min = liczba
    if liczba_max == None or liczba > liczba_max:
        liczba_max = liczba

if liczba_min != None:
    print(f"Minimalna liczba to: {liczba_min}, maksymalna liczna to: {liczba_max}")
else:
    print("Nie podałeś żadnych liczb!")