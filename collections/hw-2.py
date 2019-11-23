liczby = []

while len(liczby) < 10:
    dana = input("Wpisz liczbę lub 'koniec': ")
    dana = dana.strip()
    if not dana:
        print("Nic nie podałeś.")
        continue
    if dana.lower() == 'koniec':
        break
    if not dana.replace("-", "").isdecimal():
        print("Obsługuję tylko liczby!")
    dana = float(dana)
    liczby.append(dana)

if len(liczby) != 0:
    print(f"Średnia wprowadzonych liczb to: {sum(liczby) / len(liczby)}")
else:
    print("Nie podałeś żadnej liczby.")