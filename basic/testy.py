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

from collections import deque

ascii_min = ord(' ')
ascii_max = ord('~')

d = deque(chr(x) for x in range(ascii_min, ascii_max + 1))

print(''.join(d))
for i in range(len(d)-1):
    d.rotate(-1)
    print(''.join(d))