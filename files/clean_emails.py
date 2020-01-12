import sys


adresy = set()


with open(sys.argv[1]) as f:
    for line in f:
        adres = line.strip()
        adres = adres.lower()
        if "@" not in adres:
            continue
        elif adres.count("@") > 1:
            continue
        adresy.add(adres)


with open(sys.argv[2], 'w') as g:
    g.write(f"{sys.argv}\n")
    for adres in sorted(adresy):
        g.write(f"{adres}\n")