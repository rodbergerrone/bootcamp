class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = None # a boolean that is true if the game is over
        self.counter = 0

    def play(self, word):
        if len(self.words) == 0:
            self.words.append(word)
            self.counter += 1
            return self.words
        if len(self.words) > 0:
            last_word = self.words[-1]
            if word not in self.words and word.startswith(last_word[-1]) == True:
                self.words.append(word)
                self.counter += 1
                return self.words
            else:
                print(f"Game over! You created chain of {self.counter} words.")
                self.game_over = True
                return self.words

    def continue_playing(self, word):
        if word not in self.words and self.counter == 0:
            self.words.append(word)
            self.counter += 1
            return self.words
        elif word not in self.words and self.counter > 0:
            last_word = self.words[-1]
            if word.startswith(last_word[-1]) == True:
                self.words.append(word)
                self.counter += 1
                return self.words
            else:
                print(f"Game over! You created chain of {self.counter} words.")
                self.game_over = True
                return self.words
        else:
            print(f"Game over! You created chain of {self.counter} words.")
            self.game_over = True
            return self.words

    def restart(self):
        #self.words.clear()
        self.counter = 0
        print("Game restarted! You are building new chain. Mind all words that you have already said!")
        self.game_over = False
        return self.words

print("""------------------------------------------
This is English version of Shiritori game.
There are only three rules:
(1) First character of next word must match last character of previous word
(2) The word must not have already been said
(3) Make your mind in 10 seconds
------------------------------------------""")
ready = input("Ready: y/n?")
if ready == "y":
    game = Shiritori()
    while True:
        if game.game_over == None:
            from threading import Timer
            timeout = 10
            t = Timer(timeout, print, ["Times up!! [hit ENTER for new run or try WORD on last character of previous one to continue building chain]"])
            t.start()
            word = input("Say word in 10 sec:")
            game.play(word)
            t.cancel()
        if game.game_over == False:
            from threading import Timer
            timeout = 10
            t = Timer(timeout, print, ["Times up!! [hit ENTER for new run or try WORD on last character of previous one to continue building chain]"])
            t.start()
            word = input("Say word in 10 sec:")
            game.continue_playing(word)
            t.cancel()
        if game.game_over == True:
            game.restart()