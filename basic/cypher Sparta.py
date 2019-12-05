import textwrap

def decrypt(message):
    l = round(len(message) / stick)
    message = textwrap.fill(message, l)
    # print(message) # można usunąc aby nie pokazywać algorytm
    new_message = []
    for n in range(l):
        for linia in message.splitlines():
            new_message += linia[n]
        new_message += '\n'
    while '\n' in new_message:
        new_message.remove('\n')
    list_to_str = ' '.join(map(str,new_message))
    list_to_str = list_to_str.replace(' ', '')
    # list_to_str = textwrap.fill(list_to_str, stick) # można usunąc aby nie pokazywać algorytmu
    return list_to_str

def encrypt(message):
    message = message.replace(' ', '.')
    filler = '.'
    num_filler = stick * (len(message)//stick+1) - len(message)
    gap = filler * num_filler
    message = message + gap
    message = textwrap.fill(message, stick)
    new_message = []
    for n in range(stick):
        for linia in message.splitlines():
            new_message += linia[n]
        new_message += '\n'
    while '\n' in new_message:
        new_message.remove('\n')
    list_to_str = ' '.join(map(str,new_message))
    list_to_str = list_to_str.replace(' ', '')
    # list_to_str = textwrap.fill(list_to_str, stick) # można usunąc aby nie pokazywać algorytmu
    return list_to_str

print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Witamy w szyfratorze:
- aby odczytać wiadomość wpisz 'decrypt'
- aby zakodować wiadomość wpisz 'encrypt'
- aby zakończyć wpisz 'cokolwiek'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
o = input("Co chcesz zrobić:")
if o.lower() == 'decrypt':
    message = input("Wpisz wiadomość:")
    stick = int(input("Długość wiersza:"))
    print("Odszyfrowano:", decrypt(message))
elif o.lower() == 'encrypt':
    message = input("Wpisz wiadomość:")
    stick = int(input("Długość wiersza:"))
    print("Zaszyfrowano:", encrypt(message))
else:
    print("Do zobaczenia")