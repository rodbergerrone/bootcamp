from mathematica.algebra import matrices

def test_dodawanie_matryc():
    assert matrices.add_matrices([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_odejmowanie_matryc():
    assert matrices.sub_matrices([1, 2, 3], [3, 2, 6]) == [1, 6]