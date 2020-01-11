iterator = range(2, 13, 2).__iter__()
try:
    while True:
        print(iterator.__next__())
except StopIteration:
    pass

print()

# Generator
def od_zera_do_cztery():
    print("Zaczynamy generować!")
    yield 0
    yield 1
    yield 2
    yield 3
    yield 4
    print("Kończymy generować!")

for x in od_zera_do_cztery():
    print(x)

print()

def wspak(l):
    for element in l[::-1]:
        yield element

for x in wspak([1, 2, 3]):
    print(x)

print()

# Reversed
a = [5, 6, 7, 8, 9]
lista = "ala ma kota i psa".split()
print(list(reversed(a)))
print(list(reversed(lista)))

print()

# Enumarate
for index, slowo in enumerate(lista):
    print(f"   {index}: {slowo}")

print()

# Sorted
liczby = (9, -44, 2, 4, 141, 23, 12, 5, 6)
print(sorted(liczby))
print(sorted(liczby, reverse=True))

print()

# Zip
print(list(zip(["a", "b", "c"], [1, 2, 3])))

print()

# Map
a = [1, 2, 3]
print(list(map(str, a)))
print(list(map(float, a)))