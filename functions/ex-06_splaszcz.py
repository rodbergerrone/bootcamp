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