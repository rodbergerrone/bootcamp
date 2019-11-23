# lista = [1, -3, 45, 34, -13, 15, 33, -2]
lista = list(range(0,101,3))
lista_dodatnia = 0
lista_ujemna = 0

for i in lista:
    if i > 0:
        lista_dodatnia += 1
    elif i < 0:
        lista_ujemna += 1

print(lista)
print(f"Jest {lista_dodatnia} dodatnich i {lista_ujemna} ujemnych")