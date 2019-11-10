l1 = float(input("Podaj pierwszą liczbę: "))
l2 = float(input("Podaj drugą liczbę: "))
l3 = input("Podaj rodzaj operacji (+,-,*,/,//,%): ")

if l3 == "+":
    print(l1 + l2)
elif l3 == "-":
    print(l1 - l2)
elif l3 == "*":
    print(l1 * l2)
elif l3 == "/":
    if l2 == 0:
        print("Brak możliwości dzielenia przez zero.")
    else:
        print(l1 / l2)
elif l3 == "//":
    if l2 == 0:
        print("Brak możliwości dzielenia przez zero.")
    else:
        print(l1 // l2)
elif l3 == "%":
    print(l1 % l2)
else:
    print("Nieobsługiwana operacja.")