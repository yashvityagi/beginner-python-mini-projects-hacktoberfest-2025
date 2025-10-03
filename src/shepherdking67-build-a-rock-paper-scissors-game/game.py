# Rock-Paper-Scissors Game
# Contributed for Hacktoberfest 2025

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 💻"

def main():
    print("=== Rock-Paper-Scissors Game ===")
    player_choice = input("Enter rock, paper, or scissors: ").lower()

    if player_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice, please try again.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    print(get_winner(player_choice, computer_choice))

if __name__ == "__main__":
    main()
