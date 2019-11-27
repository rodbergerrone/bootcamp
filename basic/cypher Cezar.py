a1, a2 = "abcdefghijklmnopqrstuvwxyz1234567890", "cdefghijklmnopqrstuvwxyzab3456789012"

def decrypt(message):
    cypher = str.maketrans(a2, a1)
    return message.translate(cypher)

def encrypt(message):
    cypher = str.maketrans(a1, a2)
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
    print(f"Odszyfrowano:", decrypt(message))
elif o.lower() == 'encrypt':
    message = input("Wpisz wiadomość:")
    print(f"Zaszyfrowano:", encrypt(message))
else:
    print("Do zobaczenia")


# z zagadek: """Kqnglpg urqvmcpkg q ebvgtpcuvgl y utqfg."""

# szyfr Vinengere