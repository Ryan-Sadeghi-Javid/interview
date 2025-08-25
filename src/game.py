from .wordlist import WordList
from .evaluator import Evaluator

class Game:
    def __init__(self, wl: WordList, ev: Evaluator, word_length: int = 5, max_attempts: int = 6):
        self.wl = wl
        self.ev = ev
        self.word_length = word_length
        self.max_attempts = max_attempts

    def play_once(self, read_input=input, write_output=lambda s: print(s, end="")):
        target = self.wl.random_word()
        tries = 0
        while tries < self.max_attempts:
            write_output(f"Guess {tries+1}/{self.max_attempts}: ")
            guess = read_input().strip().lower()
            if not self.wl.is_valid(guess, self.word_length):
                write_output("Invalid guess (5-letter word from list required).\n")
                continue
            hint = self.ev.evaluate(target, guess)
            write_output("".join(hint) + "\n")
            if all(c == 'G' for c in hint):
                write_output("You win!\n"); return True
            tries += 1
        write_output(f"Out of tries. The word was: {target}\n")
        return False

if __name__ == "__main__":
    Game(WordList(), Evaluator()).play_once()