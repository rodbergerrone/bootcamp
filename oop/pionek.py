import random


class Pionek:
    def __init__(self):
        self.x = 0
        self.y = 0

    def umiesc_w_losowym_miejscu(self, plansza_wymiar_x, plansza_wymiar_y):
        self.x = random.randrange(0, plansza_wymiar_x)
        self.y = random.randrange(0, plansza_wymiar_y)

    def przesun(self, kierunek, plansza_wymiar_x=None, plansza_wymiar_y=None):
        if kierunek == 'w':
            if plansza_wymiar_y and self.y + 1 >= plansza_wymiar_y:
                return
            self.y += 1
        elif kierunek == 's':
            if self.y - 1 < 0:
                return
            self.y -= 1
        elif kierunek == 'a':
            if self.x - 1 < 0:
                return
            self.x -= 1
        elif kierunek == 'd':
            if plansza_wymiar_x and self.x + 1 >= plansza_wymiar_x:
                return
            self.x += 1


class Wojownik(Pionek):
    def __init__(self, imie):
        super().__init__()
        self.imie = imie
        self.punkty_zycia = 100
        self.sila_ataku = 15

    def zbierz_miecz(self):
        self.sila_ataku += 25

    def zbierz_pistolet(self):
        self.sila_ataku += 50

    def ulecz(self):
        self.punkty_zycia += 40


class Boss(Wojownik):
    def __init__(self, imie):
        super().__init__(imie)
        self.punkty_zycia = 200


class Miecz(Pionek):
    def __init__(self, imie):
        super().__init__()
        self.imie = imie
        self.punkty_zycia = 25


class Pistolet(Pionek):
    def __init__(self, imie):
        super().__init__()
        self.imie = imie
        self.punkty_zycia = 50


class Apteczka(Pionek):
    def __init__(self, imie):
        super().__init__()
        self.imie = imie
        self.punkty_zycia = 40


def plansza_jako_string(pionki, plansza_wymiar_x, plansza_wymiar_y):
    s = ""
    for y in range(plansza_wymiar_y - 1, -1, -1):
        for x in range(plansza_wymiar_x):
            for pionek in pionki:
                if pionek.x == x and pionek.y == y and pionek.punkty_zycia > 0:
                    s += pionek.imie[0] + " "
                    break
            else:  # nie znaleziono pionka na tym polu
                s += '. '
        s += "\n"
    return s

    # Wersja z tekstowym zaznaczeniem polożenia
    # s = ""
    # for pionek in pionki:
    #     s += f"{pionek.imie}:\t\t{pionek.x}, {pionek.y}\n"
    # return s


if __name__ == "__main__":
    wojownicy = [Wojownik("Janusz"), Wojownik("Grażyna"), Boss("Dżesika"), Boss("Seba")]
    bronie = [Pistolet("pistolet"), Pistolet("pistolet"), Miecz("miecz"), Miecz("miecz")]
    apteczki = [Apteczka("apteczka"), Apteczka("apteczka"), Apteczka("apteczka"), Apteczka("apteczka")]
    pionki = wojownicy + bronie + apteczki
    for pionek in pionki:
        pionek.umiesc_w_losowym_miejscu(10, 10)
    print(plansza_jako_string(pionki, 10, 10))
    while True:
        ruch = input("Podaj ruch [w/s/a/d] lub q by wyjść: ")
        if ruch == 'q':
            break
        wojownicy[0].przesun(ruch, 10, 10)
        wojownicy[1].przesun(random.choice("wsad"), 10, 10)
        wojownicy[2].przesun(random.choice("wsad"), 10, 10)
        wojownicy[3].przesun(random.choice("wsad"), 10, 10)
        z = "Poziom życia/siła: "
        for pionek in wojownicy:
            for apteczka in apteczki:
                if pionek.x == apteczka.x and pionek.y == apteczka.y:
                    pionek.ulecz()
                    apteczka.punkty_zycia = 0
            for bron in bronie:
                if pionek.x == bron.x and pionek.y == bron.y:
                    if bron.imie == "pistolet":
                        pionek.zbierz_pistolet()
                    if bron.imie == "miecz":
                        pionek.zbierz_miecz()
                    bron.punkty_zycia = 0
            for przeciwnik in wojownicy:
                if pionek.x == przeciwnik.x and pionek.y == przeciwnik.y:
                    if przeciwnik.imie != pionek.imie:
                        przeciwnik.punkty_zycia -= pionek.sila_ataku
                        pionek.punkty_zycia -= przeciwnik.sila_ataku
            z += f"{pionek.imie[0]}-{pionek.punkty_zycia}/{pionek.sila_ataku} "
        print(plansza_jako_string(pionki, 10, 10))
        print(z)