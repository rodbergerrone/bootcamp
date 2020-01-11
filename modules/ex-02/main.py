import przystanki
from pojazdy import kolowe, szynowe


def main():
    linie = [
        szynowe.Tramwaj(1),
        szynowe.Tramwaj(25),
        kolowe.Autobus(105),
        kolowe.Autobus(500)
    ]
    print(przystanki.zbuduj_rozklad(linie))

if __name__ == "__main__":
    main()