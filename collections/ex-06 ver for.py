lista = [11, 500, 10, 15]
liczba_min = None
liczba_max = None
index_min = None
index_max = None

print("Przed:", lista)

for x in lista:
    if liczba_min == None or x < liczba_min:
        liczba_min = x
        index_min = lista.index(x)
    if liczba_max == None or x > liczba_max:
        liczba_max = x
        index_max = lista.index(x)

lista[index_min] = liczba_max
lista[index_max] = liczba_min

print("liczba min:", liczba_min, "liczba max:", liczba_max)
print("Po:", lista)