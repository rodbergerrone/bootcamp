liczby = []
while True:
    liczby.append(input("Wpisz liczbę: "))
    if len(liczby) == 10:
        print(liczby)
        liczby = list(map(float, liczby))
        print(sum(liczby) / 10)
        break