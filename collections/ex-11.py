def lista_unikalnych_parzystych100(lista=[]):
    lista.sort()
    cyfry = {}
    for cyfra in lista:
        if cyfra in cyfry:
            cyfry[cyfra] += 1
        else:
            cyfry[cyfra] = 1
    print(f"Na liście znajdują się {lista} i występują w następującej liczbie:")
    for cyfra, ilosc in cyfry.items():
        print(f"    - '{cyfra!r}': {ilosc}""")
    cyfry_parzyste_do_100 = 0
    for cyfra_parzysta in lista:
        if cyfra_parzysta in lista and cyfra_parzysta % 2 == 0 and cyfra_parzysta in range(0, 101):
            cyfry_parzyste_do_100 += 1
    print("Ilość cyfr parzystych w przedziale 0-100:", cyfry_parzyste_do_100)

lista_unikalnych_parzystych100([6, 4, 4, 4, 3, 666, 5, 101, 99, 14, 777])