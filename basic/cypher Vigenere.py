a = "abcdefghijklmnopqrstuvwxyz1234567890"
b = "bcdefghijklmnopqrstuvwxyza2345678901"
c = "cdefghijklmnopqrstuvwxyzab3456789012"
d = "defghijklmnopqrstuvwxyzabc4567890123"
e = "defghijklmnopqrstuvwxyzabc4567890123"
f = "defghijklmnopqrstuvwxyzabc4567890123"
g = "defghijklmnopqrstuvwxyzabc4567890123"
h = "defghijklmnopqrstuvwxyzabc4567890123"
i = "defghijklmnopqrstuvwxyzabc4567890123"
j = "defghijklmnopqrstuvwxyzabc4567890123"
k = "defghijklmnopqrstuvwxyzabc4567890123"
l = "defghijklmnopqrstuvwxyzabc4567890123"
m = "defghijklmnopqrstuvwxyzabc4567890123"
n = "defghijklmnopqrstuvwxyzabc4567890123"
o = "defghijklmnopqrstuvwxyzabc4567890123"
p = "defghijklmnopqrstuvwxyzabc4567890123"
q = "defghijklmnopqrstuvwxyzabc4567890123"
r = "defghijklmnopqrstuvwxyzabc4567890123"
s = "defghijklmnopqrstuvwxyzabc4567890123"
t = "defghijklmnopqrstuvwxyzabc4567890123"
u = "defghijklmnopqrstuvwxyzabc4567890123"
w = "defghijklmnopqrstuvwxyzabc4567890123"
x = "defghijklmnopqrstuvwxyzabc4567890123"
y = "defghijklmnopqrstuvwxyzabc4567890123"
z = "defghijklmnopqrstuvwxyzabc4567890123"


def decrypt(message, keys):
    message = message.replace(' ', '').replace('.', '')
    for key in keys:
        cypher = str.maketrans(a, key)
        return message.translate(cypher)


def encrypt(message, keys):
    message = message.replace(' ', '').replace('.', '')
    # print(message)
    if len(keys) > len(message):
        keys_min = len(message) - len(keys)
        keys = keys[0:keys_min]
    else:
        keys_max = len(message) - (len(message) // len(keys) * len(keys))
        keys = keys * (len(message) // len(keys)) + keys[0:keys_max]
        print(message)
        print(keys)
    for key in keys:
        new_key = key
        cypher = str.maketrans(new_key, a)
        return message.translate(cypher)


print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Witamy w szyfratorze:
- aby odczytać wiadomość wpisz 'decrypt'
- aby zakodować wiadomość wpisz 'encrypt'
- aby zakończyć wpisz 'cokolwiek'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
o = input("Co chcesz zrobić:")
if o.lower() == 'decrypt':
    message = input("Wpisz wiadomość:")
    keys = input("Wpisz klucz:")
    print(f"Odszyfrowano:", decrypt(message, keys))
elif o.lower() == 'encrypt':
    message = input("Wpisz wiadomość:")
    keys = input("Wpisz klucz:")
    print(f"Zaszyfrowano:", encrypt(message, keys))
else:
    print("Do zobaczenia")