def formatuj1(cena):
    cena = str(cena)
    print("koszt $cena PLN,\nkwota $cena brutto".replace('$cena', cena))

def formatuj2(miasto1, miasto2, czas):
    czas = str(czas)
    print("Podróż z $miasto1 do $miasto2 zajmuje $czas h".replace('$miasto1', miasto1).replace('$miasto2', miasto2).replace('$czas', czas))

def formatuj3(powitanie, kolor):
    print("$powitanie!\nMam $kolor samochód.\nMam też $kolor rower.\nA nawet mam $kolor dom, bo $kolor to mój ulubiony kolor.".replace('$powitanie', powitanie).replace('$kolor', kolor))

formatuj1(input("Podaj cenę:"))
formatuj2(input("Podaj miejsce startu:"), input("Podaj miejsce zakończenia:"), input("Podaj czas:"))
formatuj3(input("Podaj pozdrowienie:"), input("Podaj kolor:"))