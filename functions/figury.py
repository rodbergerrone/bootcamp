def pole_trapez(wysokosc, podstawa1, podstawa2):
    return wysokosc * (podstawa1 + podstawa2) / 2

def pole_elipsa(promien, rozciagniecie):
    return (3.14 * promien ** 2) * rozciagniecie


def test_argumenty_pozycyjne():
    assert pole_trapez(10, 3, 6) == 45

def test_argumenty_nazwane():
    assert pole_trapez(wysokosc=10, podstawa1=3, podstawa2=6) == 45

def test_argumenty_nazwane_bez_kolejnosci():
    assert pole_trapez(podstawa1=3, wysokosc=10, podstawa2=6) == 45

def testy_pole_elipsy():
    assert pole_elipsa(1, 2) == 3.14 * 2