import random

def roll_dice():
    """Simulate rolling a dice and return a number between 1 and 6."""
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        input("Press Enter to roll the dice...")
        dice_number = roll_dice()
        print(f"You rolled a {dice_number}!")
        
        # Ask the user if they want to roll again
        again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing the Dice Rolling Simulator!")
            break

if __name__ == "__main__":
    main()
