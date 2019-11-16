# x = input("Wpisz coś:")
# print(count(x))

x = list()
while True:
    x += input("Wpisz cokolwiek: ")
    print(x)
    print(x[2: -2])
    print(len(x))
    if "end" in input("Wpisz 'end' aby zakończyć."):
        break