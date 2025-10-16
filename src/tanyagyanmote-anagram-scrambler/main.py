import random
from pathlib import Path


WORDS_FILE = Path(__file__).with_name("words.txt")

DEFAULT_WORDS = [
    "python", "variable", "function", "stream", "object", "module",
    "array", "string", "integer", "boolean", "class", "loop",
    "anagram", "shuffle", "random", "binary", "search", "sorting"
]

def load_words():
    if WORDS_FILE.exists():
        words = [w.strip().lower() for w in WORDS_FILE.read_text(encoding="utf-8").splitlines()]
        return [w for w in words if w and w.isalpha()]
    return DEFAULT_WORDS

def scramble(word: str) -> str:
    letters = list(word)
    for _ in range(20):
        random.shuffle(letters)
        scrambled = "".join(letters)
        if scrambled != word:
            return scrambled
    return "".join(letters)

def play_round(word: str) -> int:
    """Returns score delta for this round."""
    s = scramble(word)
    revealed = set()
    score_delta = 0

    print(f"\nScramble: {s}")
    while True:
        cmd = input("Your guess (or 'hint'/'shuffle'/'skip'/'quit'): ").strip().lower()

        if cmd == "quit":
            raise SystemExit
        if cmd == "skip":
            print(f"➡️  Skipped. The word was: {word}")
            return -1
        if cmd == "shuffle":
            s = scramble(word)
            print(f"Rescrambled: {s}")
            continue
        if cmd == "hint":
            for i, ch in enumerate(word):
                if i not in revealed:
                    revealed.add(i)
                    hint_str = "".join(ch if i in revealed else "_" for i, ch in enumerate(word))
                    print(f"Hint: {hint_str}  (length {len(word)})")
                    break
            else:
                print("No more hints available.")
            continue

        if cmd == word:
            print("✅ Correct! +2 points")
            return 2
        else:
            print("❌ Not quite. Try again, or type 'hint'.")

def main():
    print("=== Anagram Scrambler ===")
    print("Commands: hint, shuffle, skip, quit")
    words = load_words()
    random.shuffle(words)

    score = 0
    for w in words:
        try:
            score += play_round(w)
            print(f"Score: {score}")
        except SystemExit:
            break

    print("\nThanks for playing!")
    print(f"Final Score: {score}")

if __name__ == "__main__":
    main()