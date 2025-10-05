import random

# Welcome message
print("Welcome to Rock, Paper, Scissors Game!")
print("You will be playing against the computer.\n")

# Possible moves
moves = ["rock", "paper", "scissors"]

# Game loop
while True:
    # Player input
    player_move = input("Enter your move (rock, paper, scissors): ").lower()
    
    if player_move not in moves:
        print("Invalid input! Please enter rock, paper, or scissors.\n")
        continue
    
    # Computer random choice
    computer_move = random.choice(moves)
    print(f"Computer chose: {computer_move}")
    
    # Determine the winner
    if player_move == computer_move:
        print("It's a draw!\n")
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissors" and computer_move == "paper"):
        print("You win!\n")
    else:
        print("Computer wins!\n")
    
    # Ask if player wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Goodbye!")
        break
