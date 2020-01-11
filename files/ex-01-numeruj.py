import sys
print(sys.argv)


def main():
    if len(sys.argv) < 2:
        print("Użycie: numeruj.py PLIK")
        return

    try:
        with open(sys.argv[1]) as f:
            for index, line in enumerate(f):
                print(f"""{index+1}: {line.rstrip()}""")
    except FileNotFoundError:
        print("Niewłaściwa nazwa pliku!")


if __name__ == "__main__":
    main()