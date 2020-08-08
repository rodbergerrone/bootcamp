from turtle import *


bok = 60

def kwadrat():
    for i in range(4):
        fd(bok)
        left(90)
        
def plansza():
    hideturtle()
    speed(10)
    # turtle.speed(10)
    for i in range(3):
        for j in range(3):
            pd()
            kwadrat()
            pu()
            fd(bok)
        bk(3*bok)
        left(90)
        fd(bok)
        right(90)

def krzyzyk(a,b):
    color("green")
    pu()
    setx(a*bok + bok/2)
    sety(b*bok + bok/2)
    pd()
    left(45)
    for i in range(4):
        fd(bok/4)
        bk(bok/4)
        left(90)
    right(45)
    pu()

def kolko(a,b):
    color("red")
    pu()
    setx(a*bok + bok/2)
    sety(b*bok + bok/2 - bok/4)
    pd()
    circle(bok/4)

if __name__ == "__main__":
    plansza()
    pola_wyboru = ((0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2))
    ilosc_ruchow = 0
    krzyzyk_pozycje = []
    kolko_pozycje = []
    while ilosc_ruchow < 9:
        print("""Wybierz pole:
        7 | 8 | 9
        4 | 5 | 6
        1 | 2 | 3""")
        x = int(input("Wybierz gdzie postawić krzyżyk:")) - 1
        krzyzyk(pola_wyboru[x][0], pola_wyboru[x][1])
        krzyzyk_pozycje.append(pola_wyboru[x])
        print(krzyzyk_pozycje)
        y = int(input("Wybierz gdzie postawić kółko:")) - 1
        kolko(pola_wyboru[y][0], pola_wyboru[y][1])
        kolko_pozycje.append(pola_wyboru[y])
        ilosc_ruchow += 2
    print("GAME OVER - NO WINNER")
