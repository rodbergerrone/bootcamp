import random

with open('sowpods.txt', 'r') as f:
    words = list(f)

word_to_guess = random.choice(words).strip().lower()
word_to_guess_as_list = list(word_to_guess)
masked_word = "_" * len(word_to_guess)
masked_word_as_list = list(masked_word)
# print(word_to_guess_as_list)
# print(masked_word_as_list)
wrong_letters = []
wrong_count = 0

hangman = ('''
                 _____
                |     |
                      |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                      |
                      |
                      |
                     _|_''', '''
                 _____
                |     |
                O     |
                |     |
                |     |
                      |  
                     _|_''', '''
                 _____
                |     |
                O     |
               /|     |
                |     |
                      |                
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
                      |
                     _|_''', ''' 
                 _____
                |     |
                O     |
               /|\    |
                |     |
               /      |
                     _|_''', '''
                 _____
                |     |
                O     |
               /|\    |
                |     |
               / \    |
                     _|_
          HANGED BY SILLY NECK''','''
          
          
          
          
          
          
          ''')
hangman_status = 7

print(f"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Guess the word or you HANGMAN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Word to guess:
{' '.join(masked_word_as_list)}""")

while True:
    letter = input("Say letter:")
    if letter in word_to_guess:
        ilosc_powtorzonych_liter = word_to_guess.count(letter)
        ilosc_przejsc_petli = 0
        while ilosc_przejsc_petli < ilosc_powtorzonych_liter:
            pozycja = word_to_guess_as_list.index(letter)
            word_to_guess_as_list[pozycja] = "@"
            masked_word_as_list[pozycja] = letter
            ilosc_przejsc_petli += 1
        print(hangman[hangman_status])
        print(f"""{' '.join(masked_word_as_list)}
Wrong letters: {', '.join(wrong_letters)}
Continue guessing. You save your neck this time!""")
    else:
        wrong_letters.append(letter)
        wrong_count += 1
        if 4 > wrong_count >= 2:
            print(hangman[0])
            hangman_status = 0
        elif 6 > wrong_count >= 4:
            print(hangman[1])
            hangman_status = 1
        elif 8 > wrong_count >= 6:
            print(hangman[2])
            hangman_status = 2
        elif 10 > wrong_count >= 8:
            print(hangman[3])
            hangman_status = 3
        elif 12 > wrong_count >= 10:
            print(hangman[4])
            hangman_status = 4
        elif 14> wrong_count >= 12:
            print(hangman[5])
            hangman_status = 5
        elif wrong_count == 14:
            print(hangman[6])
            break
        print(f"""{' '.join(masked_word_as_list)}
Wrong letters: {', '.join(wrong_letters)}
Wrong. Getting closer to your neck!""")
    if '_' not in masked_word_as_list:
        print("Bravo. You saved your neck!")
        break