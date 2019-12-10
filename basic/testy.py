# x = input("Wpisz coś:")
# print(count(x))

# x = list()
# while True:
#     x.append(input("Wpisz cokolwiek: "))
#     print(x)
#     print(x[2: -2])
#     print(len(x))
#     if "end" in input("Wpisz 'end' aby zakończyć."):
#         break

# x = [1, 2, 3, 4]
# # print(sum(x))

x = []
# while True:
#     x.insert(0, input("Wpisz cokolwiek:"))
#     print(x)
#
# from collections import deque
#
# ascii_min = ord(' ')
# ascii_max = ord('~')
#
# d = deque(chr(x) for x in range(ascii_min, ascii_max + 1))
#
# print(''.join(d))
# for i in range(len(d)-1):
#     d.rotate(-1)
#     print(''.join(d))
#
# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# # print(l)
#
# def factional(l):
#     if l == 0:
#         return 1
#     return l * factional(l-1)
#
# l = int(input("Podaj liczbe:"))
# dict_l = {}
# for i in range(1, l+1):
#     dict_l[i] = i * i
# print(dict_l)
#
# import math
#
# def square_root():
#     C = 50
#     H = 30
#     d = []
#     while True:
#         D = input("Podaj liczbę:")
#         if D == "koniec":
#             break
#         d.append(D)
#     d = list(map(int, d))
#     q = []
#     for x in d:
#         Q = (2 * C * x) / H
#         Q = math.sqrt(Q)
#         Q = int(round(Q, 0))
#         q.append(Q)
#     return q
#
# print(square_root())
#
# l = ['without', 'hello', 'bag', 'world']
# l.sort()
# print(l)

import re
haslo = input("Podaj hasło:")
for i in haslo:
    if len(haslo) < 6 or len(haslo) > 12:
        print("Hasło niezgodne z regulaminem!")
        break
    if not re.search("[a-z]", i):
        print("Hasło niezgodne z regulaminem!")
        break
    elif not re.search("[A-Z]", i):
        print("Hasło niezgodne z regulaminem!")
        break
    elif not re.search("[1-9]", i):
        print("Hasło niezgodne z regulaminem!")
        break
    elif not re.search("[$#@]", i):
        print("Hasło niezgodne z regulaminem!")
        break
    else:
        print("Hasło poprawne!")