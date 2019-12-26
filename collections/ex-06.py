# zadanie #6 z collections:
# Napisz program zamieniajacy miejscami w zadanej liscie liczb element najwiekszy z najmniejszym.
# (źródła inspiracji: zadanie 14 z poprzedniego zjazdu; liczenie kroków w poprzedniej pracy domowej z grą czyli zadaniu 15)


lista = [99, 22, 3, 4, 1, 200, 7, 8, 9, 10, 20, 30, 40, 50, 60, 666, 80, 90, 100]
print("Przed:", lista)
print("Najmniejsza liczba:", min(lista))
print("Największa liczba:", max(lista))
mini, maxi = min(lista), max(lista)
index_min, index_max = lista.index(min(lista)), lista.index(max(lista))
lista[index_min], lista[index_max] = maxi, mini
print("Po:", lista)