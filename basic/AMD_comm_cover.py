import numpy as np


"""Na potrzeby tego skryptu zakładamy, że każdy maszt ma te same parametry poktycia.
Skrypy poprosi o dwie dane:
- a - promień pokrycia masztu
- b - dystans pomiędzy masztami"""


def single_node(r):
    return np.pi * r ** 2

def two_nodes(d, R, r):
    if d <= abs(R-r):
        # Jeden okrąg jest całkowicie zamknięty w drugim.
        return np.pi * min(R, r)**2
    if d >= r + R:
        # Oręgi w ogóle się nie pokrywają.
        nodes = np.pi * r ** 2 + np.pi * R ** 2
        return nodes

    r2, R2, d2 = r**2, R**2, d**2
    alpha = np.arccos((d2 + r2 - R2) / (2*d*r))
    beta = np.arccos((d2 + R2 - r2) / (2*d*R))
    A = (r2 * alpha + R2 * beta - 0.5 * (r2 * np.sin(2*alpha) + R2 * np.sin(2*beta)))
    nodes = np.pi * r ** 2 + np.pi * R ** 2 - A
    return nodes

def multi_nodes_inline(d, R, r, n):
    if d <= abs(R-r):
        # Jeden okrąg jest całkowicie zamknięty w drugim.
        return np.pi * min(R, r)**2
    if d >= r + R:
        # Oręgi w ogóle się nie pokrywają.
        nodes = (np.pi * r ** 2) * n
        return nodes

    r2, R2, d2 = r**2, R**2, d**2
    alpha = np.arccos((d2 + r2 - R2) / (2*d*r))
    beta = np.arccos((d2 + R2 - r2) / (2*d*R))
    A = (r2 * alpha + R2 * beta - 0.5 * (r2 * np.sin(2*alpha) + R2 * np.sin(2*beta)))
    nodes = ((np.pi * r ** 2) * n) - (A * (c - 1))
    return nodes

a = int(input("Podaj zasięg masztu w km?"))
b = int(input("Podaj odległość pomiędzy masztami w km?"))
c = int(input("Podaj ilość masztów w systemie?"))

print(f"Pokrycie pojedyńczego masztu o zasięgu {a} km w km2:")
print(single_node(a))

print(f"Pokrycie {c} masztów o zasiegu {a} km każdy, oddalonych od siebie o {b} km, w km2:")
if c<2:
    print(single_node(a))
elif c==2:
    print(two_nodes(b, a, a))
elif c>2:
    print(multi_nodes_inline(b, a, a, c))
