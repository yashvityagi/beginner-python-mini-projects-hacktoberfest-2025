# Rock Paper Scissors Game 🎮✊✋✌️

A simple **Python command-line game** where you play **Rock-Paper-Scissors** against the computer.

---

## ✨ Features
- Play against the computer 🤖
- Beginner-friendly & lightweight
- Replay option until you choose to quit

---

## ▶️ How to Run
1. Ensure you have **Python 3** installed on your system.
2. Navigate to the project folder:
cd src/adithyapathakoti-build-a-rock-paper-scissors-game/
3. Run the application:
python rock_paper_scissors.py
4. Follow the on-screen prompts to play the game.

---

## 🖥️ Sample Output
=== Rock Paper Scissors Game ===
Choose your move:
1. Rock
2. Paper
3. Scissors
Enter 1/2/3: 1

👉 You chose: Rock
🤖 Computer chose: Scissors

🏆 Result: 🎉 You Win!

Do you want to play again? (y/n): n
👋 Thanks for playing! Goodbye.

---

## 📦 Requirements
- Python 3.x
- No external libraries required
import random

options = ["Rock", "Paper", "Scissors"]
while True:
    user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
    if user_choice not in options:
        print("Invalid choice, try again.")
        continue
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        break
print("Thanks for playing!")
