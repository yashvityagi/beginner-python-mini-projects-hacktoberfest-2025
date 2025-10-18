import random
import os

QUOTES = [
    "Believe in yourself and all that you are.",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Sometimes later becomes never. Do it now.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn't just find you. You have to go out and get it.",
    "Don't stop when you're tired. Stop when you're done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Little things make big days."
]

FAVORITES_FILE = "favorites.txt"

def display_quote():
    quote = random.choice(QUOTES)
    print("\n💡 Motivational Quote of the Day:\n")
    print(f"\"{quote}\"\n")
    save = input("Do you want to save this quote to favorites? (y/n): ").strip().lower()
    if save == "y":
        save_quote(quote)

def save_quote(quote):
    with open(FAVORITES_FILE, "a") as f:
        f.write(quote + "\n")
    print("✅ Quote saved to favorites!")

def view_favorites():
    if not os.path.exists(FAVORITES_FILE):
        print("No favorites found. Save some quotes first!")
        return
    print("\n📚 Your Favorite Quotes:\n")
    with open(FAVORITES_FILE, "r") as f:
        for idx, line in enumerate(f.readlines(), 1):
            print(f"{idx}. {line.strip()}")

def main():
    while True:
        print("\n=== Motivational Quote Notifier ===")
        print("1. Show random quote")
        print("2. View favorite quotes")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == "1":
            display_quote()
        elif choice == "2":
            view_favorites()
        elif choice == "3":
            print("Goodbye! Stay motivated 💪")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
