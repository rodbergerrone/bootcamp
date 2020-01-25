import argparse

def powitaj():
    parser = argparse.ArgumentParser()
    parser.add_argument("imie", help = "your name")
    parser.add_argument("nazwisko", help = "your surname")
    parser.add_argument("--pozdrowienie", help = "how to greet", default= "Witaj")
    args = parser.parse_args()

    print()
    print(f"{args.pozdrowienie} {args.imie} {args.nazwisko}")

if __name__ == "__main__":
    powitaj()