liczby_podzielne_x = []
liczby_podzielne_y = []
for x in range(0,101):
    if x % 3 == 0 or x % 5 == 0:
        liczby_podzielne_x.append(x)
print(f"W przedziale 0-100 jest {len(liczby_podzielne_x)} podzielnych przez 3 lub 5, są to: {liczby_podzielne_x}")
for y in range(0, 101):
    if y % 3 == 0 and y % 5 == 0:
        liczby_podzielne_y.append(y)
print(f"Ale tylko {len(liczby_podzielne_y)} podzielnych jest jednocześnie przez 3 i 5, są to: {liczby_podzielne_y}")
