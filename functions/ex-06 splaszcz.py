def splaszcz(l):
    for i in l:
        if type(i) == list:
            pozycja = l.index[i]
            del l[l.index(i)]
            l[pozycja] = i
    return l
l = [1, 2, 3, [4, 5, [6]], 7]
print(splaszcz(l))
