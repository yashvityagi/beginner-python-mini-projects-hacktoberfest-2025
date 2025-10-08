import time
import random
import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_sentences():
    """Returns a list of sentences for the typing test."""
    return [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is the art of telling a computer what to do.",
        "Never underestimate the power of a good book.",
        "The sun always shines brightest after the rain.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
        "The only way to do great work is to love what you do.",
        "A journey of a thousand miles begins with a single step.",
        "Technology is best when it brings people together.",
        "Simplicity is the ultimate sophistication."
    ]

def calculate_results(prompt_text, user_text, elapsed_time):
    """Calculates WPM and accuracy."""
    # Calculate Words Per Minute (WPM)
    # Assumes average word length is 5 characters, including space
    words_typed = len(user_text) / 5
    wpm = (words_typed / elapsed_time) * 60

    # Calculate Accuracy
    correct_chars = 0
    for i in range(min(len(prompt_text), len(user_text))):
        if prompt_text[i] == user_text[i]:
            correct_chars += 1
    
    accuracy = (correct_chars / len(prompt_text)) * 100
    
    return wpm, accuracy

def main_game():
    """Main function to run the typing speed test."""
    clear_screen()
    print("======================================")
    print("      Welcome to the Typing Test!     ")
    print("======================================")
    print("\nInstructions:")
    print("1. A random sentence will be displayed.")
    print("2. Type it as quickly and accurately as you can.")
    print("3. Press Enter when you're done.")
    
    input("\nPress Enter to start the test...")

    sentences = get_sentences()
    prompt = random.choice(sentences)

    clear_screen()
    print("Type this sentence:")
    print("\n" + prompt + "\n")
    
    # Wait for the user to start typing. The input prompt itself serves this purpose.
    start_time = time.time()
    user_input = input("> ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    
    wpm, accuracy = calculate_results(prompt, user_input, elapsed_time)

    # Display the results
    clear_screen()
    print("======================================")
    print("              RESULTS                 ")
    print("======================================")
    print(f"\nTime Elapsed: {elapsed_time:.2f} seconds")
    print(f"Your Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")
    print("\n--------------------------------------")
    print("Original sentence:")
    print(prompt)
    print("\nWhat you typed:")
    print(user_input)
    print("======================================")

def run_test():
    """Controls the game loop."""
    while True:
        main_game()
        
        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again in ["yes", "no"]:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        if play_again == "no":
            print("\nThanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    run_test()
