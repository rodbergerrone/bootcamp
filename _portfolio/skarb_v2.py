# Zadanie #15 ze slajdów:
# Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o rozmiarach 10 na 10. Użytkownik może wprowadzać komendy zmieniające położenie postaci. Po każdym ruchu użytkownik powinien otrzymywać informację o tym, czy zmierza dobrym kierunku. Wyjście poza planszę oznacza koniec gry. Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na dojście do celu.
# Dodatkowo (rozwinięcie dla chętnych):
# :eight_spoked_asterisk: po wykonaniu większej liczby kroków niż dwukrotność minimalnej liczby kroków umieść skarb w nowym miejscu,
# :eight_spoked_asterisk: z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku.
# Komentarz:
# Można się poruszać góra/dół/lewo/prawo wpisując odpowiednią komendę (proponuję typowe rozwiązanie z gier - odpowiednio literki: w/s/a/d). Proponuję zignorować spadanie z planszy mimo, że jest w zadaniu na slajdzie - według mnie psuje zabawę :slightly_smiling_face:


from random import randrange
gracz_x = randrange(1, 11)
gracz_y = randrange(1, 11)
skarb_x = randrange(1, 11)
skarb_y = randrange(1, 11)
licznik = 0

print(f"""Witaj poszukiwaczu skarbów. Gdzieś tutaj jest worek złota.
Mapa ma 10 jednostek długości i 10 jednostek szerokości.
Użyj klawisza W aby iść w górę mapy.
Użyj klawisza S aby iść w dół mapy.
Użyj klawisza A aby iść w lewo.
Użyj klawisza D aby iść w prawo.
Obecnie znajdujesz się na współrzędnych: x={gracz_x}, y={gracz_y}.""")

while True:
    odleglosc_przed_ruch = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    ruch = input("Podaj kierunek [w/s/a/d]: ").lower()
    end_bad = "Spadłeś z mapy i dopadły cię dzikusy! GAME OVER :-("
    end_good = "znalazłeś worek złota! GRATULACJE :-)"
    if ruch == "w":
        gracz_y += 1
    elif ruch == "s":
        gracz_y -= 1
    elif ruch == "a":
        gracz_x -= 1
    elif ruch == "d":
        gracz_x += 1
    else:
        print("Nacisnąłeś zły przycisk! Spróbój ponownie.")
        continue

    print(f"Przeszedłeś na współrzędne: x={gracz_x}, y={gracz_y}.")
    odleglosc_po_ruch = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    licznik += 1

    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print(end_bad)
        break
    if gracz_x == skarb_x and gracz_y == skarb_y:
        print(f"Zrobiłeś {licznik} ruchów i " + end_good, f"Minimalna liczba ruchów: {odleglosc_przed_ruch}")
        break

    if randrange(0, 5) == 0:
        print("Nie wiem co Ci podpowiedzieć!")
    elif odleglosc_przed_ruch > odleglosc_po_ruch:
        print("Ciepło!")
    else:
        print("Zimno!")
    if licznik % 10 == 0:
        skarb_x = randrange(1, 11)
        skarb_y = randrange(1, 11)
        print("Tubylcy przeciągneli skarb w inne miejsce!!")
