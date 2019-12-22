class Pies:
    rasa = "Mieszkaniec"
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"Pies rasy {self.rasa}, x={self.x}, y={self.y}"

    def biegnij(self):
        self.x += 1
        self.y += 1

    def zjedz_karme(self, karma):
        pass

    def daj_glos(self):
        print("Hau hau!")

class Hart(Pies):
    rasa = "Hart"
    def biegnij(self):
        super().biegnij()
        super().biegnij()
        super().biegnij()

class Lagotto(Pies):
    rasa = "Lagotto"
    def znajdz_trufle(self):
        return "Trufla"

class Haski(Pies):
    rasa = "Haski"
    def daj_glos(self):
        print("Huuuola!")

azor = Pies()
azor.biegnij()
print(azor)
azor.daj_glos()

szybki = Hart()
szybki.biegnij()
print(szybki)
szybki.daj_glos()

dzuseppe = Lagotto()
dzuseppe.biegnij()
print(dzuseppe)
dzuseppe.daj_glos()
print(dzuseppe.znajdz_trufle())

tajga = Haski()
tajga.biegnij()
print(tajga)
tajga.daj_glos()