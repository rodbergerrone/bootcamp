a = "abcdefghijklmnopqrstuvwxyz1234567890"
b = "bcdefghijklmnopqrstuvwxyz1234567890a"
c = "cdefghijklmnopqrstuvwxyz1234567890ab"
d = "defghijklmnopqrstuvwxyz1234567890abc"
e = "efghijklmnopqrstuvwxyz1234567890abcd"
f = "fghijklmnopqrstuvwxyz1234567890abcde"
g = "ghijklmnopqrstuvwxyz1234567890abcdef"
h = "hijklmnopqrstuvwxyz1234567890abcdefg"
i = "ijklmnopqrstuvwxyz1234567890abcdefgh"
j = "jklmnopqrstuvwxyz1234567890abcdefghi"
k = "klmnopqrstuvwxyz1234567890abcdefghij"
l = "lmnopqrstuvwxyz1234567890abcdefghijk"
m = "mnopqrstuvwxyz1234567890abcdefghijkl"
n = "nopqrstuvwxyz1234567890abcdefghijklm"
o = "opqrstuvwxyz1234567890abcdefghijklmn"
p = "pqrstuvwxyz1234567890abcdefghijklmno"
q = "qrstuvwxyz1234567890abcdefghijklmnop"
r = "rstuvwxyz1234567890abcdefghijklmnopq"
s = "stuvwxyz1234567890abcdefghijklmnopqr"
t = "tuvwxyz1234567890abcdefghijklmnopqrs"
u = "uvwxyz1234567890abcdefghijklmnopqrst"
v = "vwxyz1234567890abcdefghijklmnopqrstu"
w = "wxyz1234567890abcdefghijklmnopqrstuv"
x = "xyz1234567890abcdefghijklmnopqrstuvw"
y = "yz1234567890abcdefghijklmnopqrstuvwx"
z = "z1234567890abcdefghijklmnopqrstuvwxy"

def decrypt(message, keys):
    message = message.replace(' ', '').replace('.', '')
    for key in keys:
        cypher = str.maketrans(a, key)
        return message.translate(cypher)

def encrypt(message, keys):
    message = message.replace(' ', '').replace('.', '').replace(',', '')
    if len(keys) > len(message):
        keys_min = len(message) - len(keys)
        keys = keys[0:keys_min]
    else:
        keys_max = len(message) - (len(message) // len(keys) * len(keys))
        keys = keys * (len(message) // len(keys)) + keys[0:keys_max]
        print(message)
        print(keys)
    pozycje = []
    alfabety = []
    for mess in message:
        pozycje.append(a.index(mess))
    print(pozycje)
    for key in keys:
        alfabety.append(key)
    print(alfabety)
    new_message = []
    new_message.append(a[0])
    new_message.append(b[11])
    new_message.append(a[0])
    new_message.append(b[12])
    new_message.append(a[0])
    new_message.append(b[10])
    new_message.append(a[14])
    new_message.append(b[19])
    new_message.append(a[0])
    return new_message


print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Witamy w szyfratorze:
- aby odczytać wiadomość wpisz 'decrypt'
- aby zakodować wiadomość wpisz 'encrypt'
- aby zakończyć wpisz 'cokolwiek'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
o = input("Co chcesz zrobić:")
if o.lower() == 'decrypt':
    input("Wpisz wiadomość:")
    keys = input("Wpisz klucz:")
    print(f"Odszyfrowano:", decrypt(message, keys))
elif o.lower() == 'encrypt':
    message = input("Wpisz wiadomość:")
    keys = input("Wpisz klucz:")
    print(f"Zaszyfrowano:", encrypt(message, keys))
else:
    print("Do zobaczenia")