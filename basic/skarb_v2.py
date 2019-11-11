from random import randrange
gracz_x = randrange(1, 10)
gracz_y = randrange(1, 10)
skarb_x = randrange(1, 10)
skarb_y = randrange(1, 10)
licznik = 0

print(f"""Witaj poszukiwaczu skarbów. Gdzieś tutaj jest worek złota.
Mapa ma 10 jednostek długości i 10 jednostek szerokości.
Użyj klawisza W aby iść w górę mapy.
Użyj klawisza S aby iść w dół mapy.
Użyj klawisza A aby iść w lewo.
Użyj klawisza D aby iść w prawo.
Obecnie znajdujesz się na współrzędnych: x={gracz_x}, y={gracz_y}.""")

while True:
    ruch = input("Podaj kierunek [w/s/a/d]: ")
    licznik += 1
    end_bad = "Spadłeś z mapy i dopadły cię dzikusy :-( GAME OVER"
    end_good = "znalazłeś worek złota! Gratulacje! :-)"
    if ruch == "w":
        gracz_y += 1
        print(f"Przeszedłeś na współrzędne: x={gracz_x}, y={gracz_y}.")
        if gracz_y - skarb_y >= -2 and gracz_y - skarb_y <= 2:
            print("Ciepło!")
        else:
            print("Zimno!")
    elif ruch == "s":
        gracz_y -= 1
        print(f"Przeszedłeś na współrzędne: x={gracz_x}, y={gracz_y}.")
        if gracz_y - skarb_y >= -2 and gracz_y - skarb_y <= 2:
            print("Ciepło!")
        else:
            print("Zimno!")
    elif ruch == "a":
        gracz_x -= 1
        print(f"Przeszedłeś na współrzędne: x={gracz_x}, y={gracz_y}.")
        if gracz_x - skarb_x >= -2 and gracz_x - skarb_x <= 2:
            print("Ciepło!")
        else:
            print("Zimno!")
    elif ruch == "d":
        gracz_x += 1
        print(f"Przeszedłeś na współrzędne: x={gracz_x}, y={gracz_y}.")
        if gracz_x - skarb_x >= -2 and gracz_x - skarb_x <= 2:
            print("Ciepło!")
        else:
            print("Zimno!")
    else:
        print("Nacisnąłeś zły przycisk! Spróbój ponownie.")
        continue
    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print(end_bad)
        break
    if gracz_x == skarb_x and gracz_y == skarb_y:
        print(f"Zrobiłeś {licznik} ruchów i " + end_good)
        break
    if licznik % 4 == 0:
        skarb_x = randrange(1, 10)
        skarb_y = randrange(1, 10)
        print("Tubylcy przeciągneli skarb w inne miejsce!!")