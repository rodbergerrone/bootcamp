def wiecej_niz(napis, liczba):
    ilosc_wystapien = {}
    for litera in napis:
        ilosc_wystapien[litera] = ilosc_wystapien.get(litera, 0) + 1

    wybrane = set()
    for litera, wystpienie in ilosc_wystapien.items():
        if wystpienie > liczba:
            wybrane.add(litera)
    return wybrane


def test_pusty_string():
    assert wiecej_niz('', 0) == set()
    assert wiecej_niz('', 3) == set()

def test_brak_powtorzen():
    assert wiecej_niz('abcdefghij', 1) == set()

def test_ala_ma_kota_0():
    assert wiecej_niz('ala ma kota a kot ma ale', 0) == {'t', 'o', 'e', 'l', ' ', 'k', 'm', 'a'}

def test_ala_ma_kota_3():
    assert wiecej_niz('ala ma kota a kot ma ale', 3) == {'a', ' '}