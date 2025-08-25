from typing import List

class Evaluator:
    """Compare guess to target. Return list of 'G','Y','.'; handle duplicates correctly."""
    def __init__(self) -> None:
        self.freq_table = {}

    def get_freq_table(self, target : str):
        for s in target:
            if s in self.freq_table:
                self.freq_table[s] += 1
            else:
                self.freq_table[s] = 1

    def evaluate(self, target: str, guess: str) -> List[str]:
        answer = ['.'] * 5
        target = target.upper()
        guess = guess.upper()
        self.get_freq_table(target)

        for i in range(len(guess)):
            if guess[i] == target[i]:
                answer[i] = 'G'
                self.freq_table[guess[i]] -= 1
        
        for i in range(len(guess)):
            if guess[i] != target[i]:
                if guess[i] in self.freq_table and self.freq_table[guess[i]] >= 1:
                    answer[i] = 'Y'
                    self.freq_table[guess[i]] -= 1
        
        return answer


        