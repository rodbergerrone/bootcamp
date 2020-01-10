import random


class Pionek:
    def __init__(self):
        self.x = 0
        self.y = 0

    def umiesc_w_losowym_miejscu(self, plansza_wymiar_x, plansza_wymiar_y):
        self.x = random.randrange(0, plansza_wymiar_x)
        self.y = random.randrange(0, plansza_wymiar_y)

    def przesun(self, kierunek):
        if kierunek == 'w' and self.y < plansza_wymiar_y:
            self.y += 1
        elif kierunek == 's' and self.y > 0:
            self.y -= 1
        elif kierunek == 'a' and self.x > 0:
            self.x -= 1
        elif kierunek == 'd' and self.x < plansza_wymiar_x:
            self.x += 1
        else:
            print("Ruch poza planszę. Spróbuj ponownie")

class Wojownik(Pionek):
    def __init__(self, imie):
        super().__init__()
        self.imie = imie
        self.punkty_zycia = 100


class Boss(Wojownik):
    def __init__(self, imie, punkty_zycia=200):
        super().__init__(imie)
        self.punkty_zycia = punkty_zycia


def plansza_jako_string(pionki, plansza_wymiar_x, plansza_wymiar_y):
    s = ""
    for x in range(plansza_wymiar_y):
       s += "_ " * plansza_wymiar_y
       for y in range(plansza_wymiar_x):
    #        pass
    #        # TODO: jeśli pod tymi współrzędnymi jest pionek, dopisz do s
    #        #  literę, która go reprezentuje. Jeśli nie ma - dopisz kropkę.
    #        #  Zakładamy, że w tym samym miejscu jest tylko jeden pionek.
    #        #  Uwaga: może być potrzebna pętla for
            s += "_ " * plansza_wymiar_x
    return s

    for n in range(stick):
        for linia in message.splitlines():
            new_message += linia[n]
        new_message += '\n'
    while '\n' in new_message:
        new_message.remove('\n')

    for x in range(1, 10):
        print(x, end=' ')
        for y in range(1, 10):
            print(f"{x * y: 3}", end=' ')
        print()

    # s = ""
    # for pionek in pionki:
    #     s += f"{pionek.imie}: {pionek.x}, {pionek.y}\n"
    # return s


if __name__ == "__main__":
    pionki = [Wojownik("Janusz"), Wojownik("Grażyna"), Wojownik("Brajan"), Boss("Seba")]
    print(plansza_jako_string(pionki, 20, 20))
    print()
    for pionek in pionki:
        pionek.umiesc_w_losowym_miejscu(20, 20)
    print(plansza_jako_string(pionki, 20, 20))