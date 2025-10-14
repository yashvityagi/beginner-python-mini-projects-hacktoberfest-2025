import random

def roll_dice():
    return random.randint(1, 6)

print("🎲 Dice Rolling Simulator 🎲")
while True:
    input("Press Enter to roll the dice... ")
    number = roll_dice()
    print(f"You rolled: {number}\n")
    
    again = input("Roll again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing! 👋")
        break
