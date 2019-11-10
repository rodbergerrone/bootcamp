suma_temp = 0
dzien = 1

while dzien < 8:
    suma_temp += float(input(f"Podaj temepraturę dla dnia {dzien}"))
    dzien += 1

print(f"Średnia temperatur to: {suma_temp / 7:.2f}")
