#####################
### Stringi (str) ###
#####################
# Oficjalna dokumentacja:
# https://docs.python.org/3.7/library/stdtypes.html#text-sequence-type-str


# s.upper() 	- zmienia wszystkie litery na wielkie
assert "Ala ma kota".upper() == "ALA MA KOTA"

# s.lower()	- zmienia wszystkie litery na małe
assert "ALA MA KOTA".lower() == "ala ma kota"

# s.replace(old, new) - zastępuje każde wystąpienie napisu old napisem new
assert "Ala".replace('Ala', 'Ola') == "Ola"

# s.strip() 	- usuwa początkowe i końcowe białe znaki (spacje itp)
assert "   Roger   ".strip() == "Roger"

# s.split()	- dzieli napis na poszczególne słowa, wynikiem jest lista słów
assert "Ala ma kota".split() == ['Ala', 'ma', 'kota']

# s.splitlines()  - dzieli wielo-linijkowy napis na linijki, wynikiem jest lista linijek
s = """Linia 1
Linia 2
Ostatnia linia."""
assert s.splitlines() == ["Linia 1", "Linia 2", "Ostatnia linia."]

# s.join(lista_slow)	- scala napisy z listy lista_slow w jeden napis, łącznikiem jest s
assert " - ".join(["Warszawa", "Monachium", "Nowy Jork"]) == "Warszawa - Monachium - Nowy Jork"

# s.count(sub) 	- zlicza wystąpienie napisu sub w napisie s
assert "We are living in yellow submarine, yellow submarine".count('sub') == 2

# s.index(sub)	- podaje pozycję, na której zaczyna się napis sub w napisie s (jeśli nie znajdzie zwraca błąd)
assert "We are living in yellow submarine, yellow submarine".index('sub') == 24

# s.find(sub)		- jak index tylko jeśli nie znajdzie, to zwraca -1
assert "We are living in yellow submarine, yellow submarine".find('sub') == 24

# s.find(sub, start, end) - find z podaniem opcjonalnych argumentów, wyszukuje w s[start:end]
assert "We are living in yellow submarine, yellow submarine".index('sub', 20, 30) == 24

# s.startswith(sub) - sprawdza, czy s zaczyna się od napisu sub
assert "We are living in yellow submarine, yellow submarine".startswith('sub') == False

# s.isdigit() 	- sprawdza czy wszystkie znaki są cyframi
assert "We are living in yellow submarine, yellow submarine".isdigit() == False

# s.islower() 	- sprawdza czy wszystkie litery są małe
assert "We are living in yellow submarine, yellow submarine".islower() == False

# s.isupper() 	- sprawdza czy wszystkie litery są duże
assert "SUBMARINE".isupper() == True

# sub in s        - sprwadza czy napis s zawiera napis sub
assert "sun" in "sunshine"
assert not ("san" in "sunshine")

# len(s)        - zwraca ilość liter
assert len("Skok") == 4

# s[index]      - zwraca literę o podanym indeksie
assert "Submarine"[4] == 'a'

# s[indeksStart:indeksStop]
assert "Submarine"[4:6] == 'ar'

# s[indeksStart::krok]
assert "Submarine"[2::2] == 'baie'

# s[:indeksStop]
assert "Submarine"[:3] == 'Sub'


####################
### Listy (list) ###
####################
# Oficjalna dokumentacja:
# https://docs.python.org/3.7/library/stdtypes.html#sequence-types-list-tuple-range


# list(s) 	- konwertuje sekwencję s na listę
assert list((1,2,3)) == [1, 2, 3]

# l.append(x) 	- dodaje nowy element x na końcu l, nic nie zwraca!
l = [1]
l.append(2)
assert l == [1, 2]

# l.extend(t) 	- dodaje nową listę t na końcu l, nic nie zwraca!
t = [2, 3, 4]
l.extend(t)
assert l == [1, 2, 2, 3, 4]

# l.count(x) 	- zlicza ilość wystąpień x w l
assert l.count(2) == 2

# l.index(x) 	- zwraca najmniejszy indeks i, gdzie l[i] == x
assert l.index(2) == 1

# l.pop(i) 	- zwraca element o indeksie i jednocześnie usuwając go z listy
l.pop(2)
assert l == [1, 2, 3, 4]

# l.remove(x) 	- usuwa z listy l pierwsze wystąpienie elementu x (jeśli nie znajdzie zwraca błąd), nic nie zwraca!
l.remove(1)
assert l == [2, 3, 4]

# l.copy()       - tworzy kopię - zwraca nową listę. To samo co l[:]. Trudno napisać na to ciekawy test :)
assert [1, 2, 3].copy() == [1, 2, 3]

# l.reverse() 	- odwraca kolejność elementów l "w miejscu" (czyli modyfikuje listę), nic nie zwraca!
l = [2, 1, 3, 0]
l.reverse()
assert l == [0, 3, 1, 2]

# l.sort() 	- sortuje elementy l "w miejscu" (czyli modyfikuje listę) - elementy muszą dać się porównywać (np. int i float), nic nie zwraca!
l = [2, 1, 3, 0]
l.sort()
assert l == [0, 1, 2, 3]

# del l[i]   - usuwa element o indeksie i z listy, nic nie zwraca!
l = [1, 2, 3]
del l[1]
assert l == [1, 3]

# x in l     - sprawdza czy x jest elementem listy
assert 3 in l

# len(l)        - zwraca ilość elementów
assert len(l) == 2


print("Wszystko poszło poprawnie!")