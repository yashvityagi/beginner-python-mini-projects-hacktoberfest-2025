"""
Hangman - Beginner-friendly command-line game

How to play:
- Guess the secret word one letter at a time.
- You have limited wrong guesses (6 by default).
- Type a single letter and press Enter. Repeat until you win or lose.

Run:
  python main.py

Optional:
  python main.py --word fruits  # pick a category (simple built-in lists)
  python main.py --max-mistakes 8

This file contains both the game implementation and a tiny CLI.
"""
from __future__ import annotations
import argparse
import random
import string
from dataclasses import dataclass, field
from typing import Iterable, Set, List


DEFAULT_WORDS = {
    "animals": ["cat", "dog", "tiger", "zebra", "lion", "panda", "shark"],
    "fruits": ["apple", "banana", "grape", "mango", "orange", "peach"],
    "colors": ["red", "green", "blue", "yellow", "purple", "orange"],
}

FALLBACK_WORDS = [
    "python", "hangman", "open", "source", "github", "code", "debug", "simple",
]


@dataclass
class HangmanGame:
    secret_word: str
    max_mistakes: int = 6
    guessed: Set[str] = field(default_factory=set)
    mistakes: int = 0

    def masked_word(self) -> str:
        return " ".join(ch if ch in self.guessed else "_" for ch in self.secret_word)

    def guess(self, letter: str) -> bool:
        letter = letter.lower()
        if not letter or len(letter) != 1 or letter not in string.ascii_lowercase:
            raise ValueError("Please guess a single letter a-z.")
        if letter in self.guessed:
            return False  # already guessed
        self.guessed.add(letter)
        if letter not in self.secret_word:
            self.mistakes += 1
            return False
        return True

    def won(self) -> bool:
        return all(ch in self.guessed for ch in self.secret_word)

    def lost(self) -> bool:
        return self.mistakes >= self.max_mistakes


def pick_word(category: str | None, rng: random.Random | None = None) -> str:
    rng = rng or random.Random()
    if category and category in DEFAULT_WORDS:
        return rng.choice(DEFAULT_WORDS[category])
    pool = [w for words in DEFAULT_WORDS.values() for w in words] or FALLBACK_WORDS
    return rng.choice(pool)


def draw_gallows(mistakes: int) -> List[str]:
    # Simple ASCII gallows with 7 states (0..6)
    stages = [
        [
            r" +---+",
            r" |   |",
            r"     |",
            r"     |",
            r"     |",
            r"     |",
            r"======="
        ],
        [
            r" +---+",
            r" |   |",
            r" O   |",
            r"     |",
            r"     |",
            r"     |",
            r"======="
        ],
        [
            r" +---+",
            r" |   |",
            r" O   |",
            r" |   |",
            r"     |",
            r"     |",
            r"======="
        ],
        [
            r" +---+",
            r" |   |",
            r" O   |",
            r"/|   |",
            r"     |",
            r"     |",
            r"======="
        ],
        [
            r" +---+",
            r" |   |",
            r" O   |",
            r"/|\  |",
            r"     |",
            r"     |",
            r"======="
        ],
        [
            r" +---+",
            r" |   |",
            r" O   |",
            r"/|\  |",
            r"/    |",
            r"     |",
            r"======="
        ],
        [
            r" +---+",
            r" |   |",
            r" O   |",
            r"/|\  |",
            r"/ \  |",
            r"     |",
            r"======="
        ],
    ]
    idx = max(0, min(mistakes, len(stages) - 1))
    return stages[idx]


def play_cli(secret_word: str, max_mistakes: int) -> None:
    game = HangmanGame(secret_word=secret_word, max_mistakes=max_mistakes)
    print("Welcome to Hangman!")
    while not (game.won() or game.lost()):
        print()
        for line in draw_gallows(game.mistakes):
            print(line)
        print(f"Word: {game.masked_word()}")
        print(f"Guessed: {' '.join(sorted(game.guessed)) if game.guessed else '-'}")
        print(f"Mistakes: {game.mistakes}/{game.max_mistakes}")

        guess = input("Guess a letter: ").strip().lower()
        try:
            hit = game.guess(guess)
        except ValueError as e:
            print(e)
            continue
        if hit:
            print("Good guess!")
        else:
            if guess in string.ascii_lowercase:
                if guess in game.secret_word:
                    # already guessed duplicate
                    print("You already tried that letter.")
                else:
                    print("Nope.")
            else:
                print("Please enter a letter a-z.")

    print()
    for line in draw_gallows(game.mistakes):
        print(line)
    if game.won():
        print(f"You won! The word was '{game.secret_word}'.")
    else:
        print(f"You lost. The word was '{game.secret_word}'. Better luck next time!")


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Play a simple Hangman game.")
    parser.add_argument("--word", dest="category", choices=list(DEFAULT_WORDS.keys()),
                        help="Choose a word category (random word picked from it).")
    parser.add_argument("--max-mistakes", type=int, default=6,
                        help="Maximum wrong guesses before losing (default: 6).")
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = parse_args()
    word = pick_word(args.category)
    play_cli(secret_word=word, max_mistakes=args.max_mistakes)
