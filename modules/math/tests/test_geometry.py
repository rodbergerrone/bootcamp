from mathematica.geometry import figures

def test_pole_kwadrat():
    assert figures.square_area(2) == 4

def test_pole_trojkat():
    assert figures.triangle_area(2, 1) == 1