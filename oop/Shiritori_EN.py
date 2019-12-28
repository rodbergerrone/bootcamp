class Shiritori:
    def __init__(self):
        self.words = []
        self.game_over = None # a boolean that is true if the game is over

    def play(self, word):
        if len(self.words) == 0:
            self.words.append(word)
            return self.words
        if len(self.words) > 0:
            last_word = self.words[-1]
            if word not in self.words and word.startswith(last_word[-1]) == True:
                self.words.append(word)
                return self.words
            else:
                print("Game over")
                self.game_over = True
                return self.words

    def restart(self):
        self.words.clear()
        print("Game restarted")
        self.game_over = False
        return self.words


if __name__ == "__main__":
    game = Shiritori()
    print(game.play("apple"))
    print(game.play("ear"))
    print(game.play("rhino"))
    print(game.play("corn"), "'Corn' nie zaczyna się na 'o'")
    game.restart()
    print(game.words)
    print(game.play("hostess"))
    print(game.play("stash"))
    print(game.play("hostess"), "Już był taki wyraz 'hostess'")