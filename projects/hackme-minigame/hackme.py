#!/usr/bin/env python3
"""
Simple Codebreaker Game 🕵️

How to Play:
- Guess the secret 3-digit code (digits may repeat).
- You have 6 attempts.
- Feedback after each guess:
    ✅ = correct digit in the correct position
    ⚠️ = digit is in the code but in the wrong position
    ❌ = digit is not in the code
Example:
    Secret: 123, Guess: 321 → ⚠️3 ⚠️2 ⚠️1
"""

import random

def generate_code():
    """Generate a random 3-digit code."""
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

def give_feedback(secret, guess):
    """Return feedback for a guess vs secret."""
    secret_list = list(secret)
    feedback = [''] * len(guess)

    # ✅ Correct position
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            feedback[i] = '✅'
            secret_list[i] = None

    # ⚠️ Wrong place or ❌ Not present
    for i in range(len(guess)):
        if feedback[i]:
            continue
        if guess[i] in secret_list:
            feedback[i] = '⚠️'
            secret_list[secret_list.index(guess[i])] = None
        else:
            feedback[i] = '❌'

    # Combine emojis with digits
    return ' '.join(f"{feedback[i]}{guess[i]}" for i in range(len(guess)))

def play_game():
    print("=== CODEBREAKER ===")
    print("Can you guess the 3-digit code?")
    print("✅ = correct spot, ⚠️ = wrong spot, ❌ = not in code\n")

    secret = generate_code()
    attempts = 6

    while attempts > 0:
        guess = input(f"[{attempts} attempts left] Enter 3 digits: ").strip()

        if not guess.isdigit() or len(guess) != 3:
            print("Please enter exactly 3 digits (e.g., 042).")
            continue

        if guess == secret:
            print("ACCESS GRANTED! ✅ You cracked the code!")
            return

        print(give_feedback(secret, guess))
        attempts -= 1

    print(f"ACCESS DENIED! The code was {secret}.")

if __name__ == "__main__":
    play_game()
