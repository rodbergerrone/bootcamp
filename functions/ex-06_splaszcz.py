# Zadanie #6 z functions:
# Zaimplementuj funkcję spłaszczającą podaną listę.
# Przykład użycia:
# >>> splaszcz([1, 2, 3, [4, 5, [6]], 7])
# [1, 2, 3, 4, 5, 6, 7]
# Myślę, że przykład użycia lepiej tłumaczy czym jest "spłaszczanie" niż jakiś opis tekstowy - ale jak dla kogoś pozostaje to
# niejasne, to dawajcie znać. Do wykonania tego zadania będzie potrzebne sprawdzenie czy dana wartość jest listą.
# Robimy to tak: isinstance(zmienna, list)  - takie wywołanie funkcji zwraca True albo False, w zależności od tego,
# czy zmienna przechowuje listę


def splaszcz(lista):
    result = []
    for element in lista:
        if isinstance(element, list):
            for subelement in splaszcz(element): #rekurencja
                result.append(subelement)
        else:
            result.append(element)
    return result


def test_flat_list():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]

def test_one_embedded_list():
    assert splaszcz([1, [2, 3]]) == [1, 2, 3]

def test_two_embedded_list():
    assert splaszcz([1, [2, [3, 4]]]) == [1, 2, 3, 4]

def test_x_embedded_list():
    assert splaszcz([[1, 2], [3, [4, 5]]]) == [1, 2, 3, 4, 5]