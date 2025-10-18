import random
import time
import json
import os

class AdvancedNumberGuessingGame:
    def __init__(self):
        self.high_scores = self.load_high_scores()
        self.player_name = ""
        self.difficulty_settings = {
            "easy": {"range": (1, 50), "attempts": 10, "points_multiplier": 1},
            "medium": {"range": (1, 100), "attempts": 7, "points_multiplier": 2},
            "hard": {"range": (1, 200), "attempts": 5, "points_multiplier": 3},
            "expert": {"range": (1, 500), "attempts": 3, "points_multiplier": 5}
        }
    
    def load_high_scores(self):
        """Load high scores from file"""
        try:
            if os.path.exists("high_scores.json"):
                with open("high_scores.json", "r") as f:
                    return json.load(f)
        except:
            pass
        return {}
    
    def save_high_scores(self):
        """Save high scores to file"""
        try:
            with open("high_scores.json", "w") as f:
                json.dump(self.high_scores, f, indent=2)
        except:
            print("Could not save high scores.")
    
    def display_welcome(self):
        """Display welcome message and rules"""
        print("🎯" * 50)
        print("          ADVANCED NUMBER GUESSING GAME")
        print("🎯" * 50)
        print("\nRules:")
        print("- Guess the secret number within limited attempts")
        print("- Higher difficulty = more points")
        print("- Use hints wisely (costs points)")
        print("- Try to beat the high score!")
        print("-" * 50)
    
    def get_player_name(self):
        """Get and validate player name"""
        while True:
            name = input("Enter your name: ").strip()
            if name and len(name) <= 20:
                self.player_name = name
                break
            print("Please enter a valid name (1-20 characters)")
    
    def choose_difficulty(self):
        """Let player choose difficulty level"""
        print("\n🎮 DIFFICULTY LEVELS:")
        for level, settings in self.difficulty_settings.items():
            min_num, max_num = settings["range"]
            attempts = settings["attempts"]
            print(f"  {level.upper()}: Numbers {min_num}-{max_num}, {attempts} attempts")
        
        while True:
            choice = input("\nChoose difficulty (easy/medium/hard/expert): ").lower()
            if choice in self.difficulty_settings:
                return choice
            print("Invalid choice! Please select from: easy, medium, hard, expert")
    
    def provide_hint(self, guess, secret_number, attempts_left, difficulty):
        """Provide intelligent hints based on the game state"""
        hint_cost = 5 * self.difficulty_settings[difficulty]["points_multiplier"]
        
        print(f"\n💡 HINT MENU (costs {hint_cost} points)")
        print("1. Is it even or odd?")
        print("2. How close am I?")
        print("3. First digit of the number")
        print("4. Cancel")
        
        while True:
            try:
                choice = int(input("Choose hint (1-4): "))
                if choice == 1:
                    return f"The number is {'even' if secret_number % 2 == 0 else 'odd'}", hint_cost
                elif choice == 2:
                    difference = abs(guess - secret_number)
                    if difference <= 5:
                        closeness = "very close"
                    elif difference <= 15:
                        closeness = "close"
                    elif difference <= 30:
                        closeness = "far"
                    else:
                        closeness = "very far"
                    return f"You're {closeness} to the number", hint_cost
                elif choice == 3:
                    first_digit = int(str(secret_number)[0])
                    return f"The number starts with {first_digit}", hint_cost
                elif choice == 4:
                    return None, 0
                else:
                    print("Please choose 1-4")
            except ValueError:
                print("Please enter a valid number")
    
    def calculate_score(self, attempts_used, total_attempts, difficulty, hints_used, time_taken):
        """Calculate score based on performance"""
        base_points = 100
        multiplier = self.difficulty_settings[difficulty]["points_multiplier"]
        
        # Points for attempts left
        attempt_bonus = (total_attempts - attempts_used) * 10
        
        # Points for quick solving
        time_bonus = max(0, 50 - (time_taken // 5))
        
        # Penalty for hints
        hint_penalty = hints_used * 5 * multiplier
        
        score = (base_points + attempt_bonus + time_bonus) * multiplier - hint_penalty
        return max(0, score)
    
    def play_round(self, difficulty):
        """Play one round of the game"""
        settings = self.difficulty_settings[difficulty]
        min_num, max_num = settings["range"]
        max_attempts = settings["attempts"]
        
        secret_number = random.randint(min_num, max_num)
        attempts = 0
        hints_used = 0
        start_time = time.time()
        previous_guesses = []
        
        print(f"\n🔢 I'm thinking of a number between {min_num} and {max_num}")
        print(f"💫 You have {max_attempts} attempts to guess it!")
        
        while attempts < max_attempts:
            attempts_left = max_attempts - attempts
            print(f"\nAttempts left: {attempts_left}")
            
            if previous_guesses:
                print(f"Previous guesses: {previous_guesses[-5:]}")  # Show last 5 guesses
            
            try:
                guess = int(input(f"Enter your guess ({min_num}-{max_num}): "))
                
                if guess < min_num or guess > max_num:
                    print(f"Please enter a number between {min_num} and {max_num}")
                    continue
                
                previous_guesses.append(guess)
                attempts += 1
                
                if guess == secret_number:
                    time_taken = time.time() - start_time
                    score = self.calculate_score(attempts, max_attempts, difficulty, hints_used, time_taken)
                    print(f"\n🎉 CONGRATULATIONS {self.player_name.upper()}! 🎉")
                    print(f"✅ You guessed the number {secret_number} in {attempts} attempts!")
                    print(f"⏰ Time taken: {time_taken:.1f} seconds")
                    print(f"🏆 Score: {score} points")
                    return score
                
                # Give feedback
                difference = abs(guess - secret_number)
                if guess < secret_number:
                    feedback = "Too low"
                else:
                    feedback = "Too high"
                
                # Additional temperature hints
                if difference <= 5:
                    temp = "🔥 BOILING HOT!"
                elif difference <= 15:
                    temp = "☀️ Hot"
                elif difference <= 30:
                    temp = "🌤️ Warm"
                elif difference <= 50:
                    temp = "❄️ Cold"
                else:
                    temp = "🧊 FREEZING COLD!"
                
                print(f"{feedback}! {temp}")
                
                # Offer hint every 2 attempts
                if attempts % 2 == 0 and attempts_left > 1:
                    hint_choice = input("Would you like a hint? (y/n): ").lower()
                    if hint_choice == 'y':
                        hint, cost = self.provide_hint(guess, secret_number, attempts_left, difficulty)
                        if hint:
                            print(f"💡 Hint: {hint}")
                            hints_used += 1
                            # In a full implementation, you'd deduct cost from score
                
            except ValueError:
                print("Please enter a valid number!")
        
        # Player lost
        time_taken = time.time() - start_time
        print(f"\n💀 GAME OVER! The number was {secret_number}")
        print(f"⏰ Time taken: {time_taken:.1f} seconds")
        return 0
    
    def update_high_scores(self, score):
        """Update high scores if current score is better"""
        if self.player_name not in self.high_scores or score > self.high_scores[self.player_name]:
            self.high_scores[self.player_name] = score
            self.save_high_scores()
            print("🏆 NEW HIGH SCORE! 🏆")
    
    def display_high_scores(self):
        """Display current high scores"""
        print("\n🏅 HIGH SCORES 🏅")
        print("-" * 30)
        if not self.high_scores:
            print("No high scores yet!")
            return
        
        sorted_scores = sorted(self.high_scores.items(), key=lambda x: x[1], reverse=True)
        for i, (name, score) in enumerate(sorted_scores[:5], 1):
            print(f"{i}. {name}: {score} points")
    
    def play_game(self):
        """Main game loop"""
        self.display_welcome()
        self.get_player_name()
        
        while True:
            difficulty = self.choose_difficulty()
            score = self.play_round(difficulty)
            
            if score > 0:
                self.update_high_scores(score)
            
            self.display_high_scores()
            
            play_again = input("\nWould you like to play again? (y/n): ").lower()
            if play_again != 'y':
                print(f"\nThanks for playing, {self.player_name}! 👋")
                break

# Run the game
if __name__ == "__main__":
    game = AdvancedNumberGuessingGame()
    game.play_game()