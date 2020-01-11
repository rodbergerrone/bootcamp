from mathematica.algebra import matrices2

def main():
    macierz1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    macierz2 = [
        [3, 1, 7],
        [4, 2, 6],
        [7, 4, 9],
    ]
    print(f"""Suma matryc {matrices2.add_matrices(macierz1, macierz2)}
Różnica matryc {matrices2.sub_matrices(macierz1, macierz2)}""")


if __name__ == "__main__":
    main()