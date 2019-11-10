import datetime
x = datetime.datetime.now()
rok = int(input("Podaj rok urodzenia: "))
wiek = x.year - rok
if wiek >= 18:
    print("Jesteś pełnoletni. Zapraszamy!")
else:
    print("Nie masz jeszcze 18 lat!")