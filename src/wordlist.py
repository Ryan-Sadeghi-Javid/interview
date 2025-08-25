from pathlib import Path
import random

class WordList:
    def __init__(self, path: str = "words.txt"):
        text = Path(path).read_text(encoding="utf-8")
        self.words = [w.strip().lower() for w in text.splitlines() if w.strip()]
        self.allowed = set(self.words)

    def random_word(self) -> str:
        return random.choice(self.words)

    def is_valid(self, guess: str, length: int = 5) -> bool:
        return guess.isalpha() and len(guess) == length and guess.lower() in self.allowed
