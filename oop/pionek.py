import random

class Pionek:
    def __init__(self):
        self.x = 0
        self.y = 0
    #umieść w losowym miejscu
    def move(self, direction):
        if direction == "w":
            self.y +=1
        if direction == "s":
            self.y -= 1
        if direction == "d":
            self.x += 1
        if direction == "a":
            self.x -=1

class Wojownik(Pionek):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.life = 100

class Boss(Wojownik):
    def __init__(self, name, life_points=200):
        super().__init__(name)
        self.life_points = life_points

pionki = [Wojownik("Janusz"), Wojownik("Grażyna"), Wojownik("Brajan"), Boss("Seba")]
for pionek in pionki:
    print(f"{pionek.name}\t\t{pionek.x}, {pionek.y}")
for _ in range (10):
    for pionek in pionki:
        pionek.move(random.choice("wsda"))