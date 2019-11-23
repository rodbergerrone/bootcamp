lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Przed:", lista)
liczba_min = None
liczba_max = None
for liczba in lista:
    if liczba_min == None or liczba < liczba_min:
        liczba_min = liczba
        print("Liczba min:", liczba_min)
    elif liczba_max == None or liczba > liczba_max:
        liczba_max = liczba
        print("Liczba max:", max(lista))
lista[lista.index(liczba_min)] = liczba_max
lista[lista.index(liczba_max)] = liczba_min
print("Po:", lista)

# max(lista)
# min(lista)
# lista.index()

# zamienić miejscami najmniejszą i największą

