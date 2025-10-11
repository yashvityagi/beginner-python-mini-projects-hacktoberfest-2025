import random

def get_user_choice():
    """Get and validate user's choice."""
    while True:
        user_input = input("Enter your move (rock/paper/scissors) or 'q' to quit: ").lower().strip()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        elif user_input == 'q':
            return 'q'
        else:
            print("Invalid input. Please enter rock, paper, scissors, or 'q' to quit.")

def get_computer_choice():
    """Generate computer's random choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user, computer):
    """Determine the winner of the round."""
    if user == computer:
        return 'draw'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    """Main game loop with scoring."""
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors! Play against the computer.")
    print("Type 'q' at any time to quit.\n")
    
    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            break
        
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'draw':
            print("It's a draw!")
        elif winner == 'user':
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        print(f"Current score - You: {user_score}, Computer: {computer_score}\n")
    
    print(f"\nFinal score - You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game overall.")
    elif computer_score > user_score:
        print("Computer won the game overall. Better luck next time!")
    else:
        print("The game ended in a tie overall.")

# Run the game
if __name__ == "__main__":
    play_game()
