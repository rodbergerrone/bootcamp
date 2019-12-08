def encrypt(message, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in message]
    new_message = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        new_message += chr(value + 65)
    return new_message

def decrypt(message, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in message]
    new_message = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        new_message += chr(value + 53)
    return new_message


print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Witamy w szyfratorze:
- aby odczytać wiadomość wpisz 'decrypt'
- aby zakodować wiadomość wpisz 'encrypt'
- aby zakończyć wpisz 'cokolwiek'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
o = input("Co chcesz zrobić:")
if o.lower() == 'decrypt':
    message = input("Wpisz wiadomość:")
    key = input("Wpisz klucz:")
    print(f"Odszyfrowano:", decrypt(message, key))
elif o.lower() == 'encrypt':
    message = input("Wpisz wiadomość:")
    key = input("Wpisz klucz:")
    print(f"Zaszyfrowano:", encrypt(message, key))
else:
    print("Do zobaczenia")