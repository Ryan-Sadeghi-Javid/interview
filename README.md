# CLI Wordle (Mini) — Pairing Prompt
Build a tiny, testable CLI Wordle:
- 5-letter target from `words.txt`
- 6 guesses
- Hints per letter: G (right spot), Y (wrong spot), . (absent)
- Validate: alpha, length 5, and in list

## Run
python -m src.game

## Test
pytest -q

## Git Flow (do these during pairing)
git checkout -b feat/cli-wordle
# implement Evaluator + tests → commit
# implement WordList/Game + words.txt → commit
git push -u origin feat/cli-wordle
# open PR titled: "CLI Wordle (minimal playable)"
