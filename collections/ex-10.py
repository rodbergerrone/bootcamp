napis = "Oko za oko, ząb za ząb"
print(napis)
literki = {}
for literka in napis:
    literka = literka.lower()
    if literka in literki:
        literki[literka] += 1
    else:
        literki[literka] = 1
for literka, ilosc in literki.items():
    print(f"- {literka!r}: {ilosc}")