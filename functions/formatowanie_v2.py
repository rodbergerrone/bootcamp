def formatuj(*args, **kwargs):
    result = "\n".join(args)
    for nazwa, wartosc in kwargs.items():
        result = result.replace("$"+nazwa, str(wartosc))
    return result


def test_formatuj_single_line_with_kwargs():
    expected = 'Podróż z Los Angeles do Yorktown zajmuje 5 h'
    assert formatuj('Podróż z $miasto1 do $miasto2 zajmuje $czas h', miasto1="Los Angeles", miasto2="Yorktown", czas=5) == expected