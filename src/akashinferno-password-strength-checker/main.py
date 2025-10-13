import re
import getpass


def check_password_strength(password):
    """
    Check password strength and return score with improvement suggestions.
    """
    score = 0
    feedback = []
    
    # Check length
    length = len(password)
    if length >= 12:
        score += 3
    elif length >= 8:
        score += 2
        feedback.append("💡 Consider making it longer (12+ characters is better)")
    else:
        score += 1
        feedback.append("❌ Password is too short (minimum 8 characters, recommended 12+)")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters (a-z)")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Add numbers (0-9)")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]\\;/~`]', password):
        score += 2
    else:
        feedback.append("❌ Add special characters (!@#$%^&* etc.)")
    
    # Check for common patterns (bonus deduction)
    common_patterns = [
        r'123', r'abc', r'password', r'qwerty', 
        r'111', r'000', r'admin', r'letmein'
    ]
    
    for pattern in common_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            score -= 1
            feedback.append("⚠️  Avoid common patterns like '123', 'abc', 'password', etc.")
            break
    
    # Check for repeated characters
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        feedback.append("⚠️  Avoid repeating the same character multiple times")
    
    # Ensure score is within bounds
    score = max(0, min(score, 10))
    
    return score, feedback


def get_strength_rating(score):
    """
    Return strength rating based on score.
    """
    if score >= 8:
        return "🔒 STRONG", "green"
    elif score >= 5:
        return "🔓 MODERATE", "yellow"
    else:
        return "⚠️  WEAK", "red"


def display_score_bar(score, max_score=10):
    """
    Display a visual score bar.
    """
    filled = int((score / max_score) * 20)
    bar = "█" * filled + "░" * (20 - filled)
    return f"[{bar}] {score}/{max_score}"


def main():
    """
    Main function to run the password strength checker.
    """
    print("=" * 50)
    print("🔐 PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    print()
    
    # Get password input (hidden for security)
    print("Enter your password (input will be hidden):")
    password = getpass.getpass("Password: ")
    
    if not password:
        print("❌ Password cannot be empty!")
        return
    
    print()
    print("Analyzing your password...")
    print()
    
    # Check password strength
    score, feedback = check_password_strength(password)
    strength, color = get_strength_rating(score)
    
    # Display results
    print("=" * 50)
    print("RESULTS:")
    print("=" * 50)
    print()
    print(f"Strength: {strength}")
    print(f"Score: {display_score_bar(score)}")
    print()
    
    # Display feedback
    if feedback:
        print("📋 Suggestions to improve your password:")
        print()
        for suggestion in feedback:
            print(f"  {suggestion}")
    else:
        print("✅ Great! Your password is strong!")
    
    print()
    print("=" * 50)
    
    # Additional tips
    print()
    print("💡 Password Tips:")
    print("  • Use at least 12 characters")
    print("  • Mix uppercase, lowercase, numbers, and symbols")
    print("  • Avoid personal information (names, birthdays)")
    print("  • Don't reuse passwords across sites")
    print("  • Consider using a passphrase (e.g., 'Coffee@Morning#2025')")
    print()


if __name__ == "__main__":
    main()
