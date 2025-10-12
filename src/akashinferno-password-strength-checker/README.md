# 🔐 Password Strength Checker

A simple yet effective CLI tool that analyzes password strength and provides actionable feedback to help users create more secure passwords.

## 📋 Description

This password strength checker evaluates passwords based on multiple security criteria and provides a comprehensive score along with specific suggestions for improvement. It's designed to help users understand what makes a strong password and how to enhance their password security.

## ✨ Features

### Core Functionality
- **Secure Input**: Password input is hidden while typing for privacy
- **Comprehensive Scoring**: Passwords are scored out of 10 points based on multiple criteria
- **Visual Feedback**: Displays an intuitive progress bar showing password strength visually
- **Strength Rating**: Categorizes passwords as WEAK 🔓, MODERATE 🔓, or STRONG 🔒

### Password Criteria Checked

#### Positive Factors (Add Points):
- ✅ **Length**: 
  - 12+ characters: +3 points
  - 8-11 characters: +2 points
  - Less than 8: +1 point (with warning)
- ✅ **Lowercase letters** (a-z): +1 point
- ✅ **Uppercase letters** (A-Z): +1 point
- ✅ **Numbers** (0-9): +1 point
- ✅ **Special characters** (!@#$%^&* etc.): +2 points

#### Negative Factors (Deduct Points):
- ❌ **Common patterns**: Detects patterns like "123", "abc", "password", "qwerty", "admin" (-1 point)
- ❌ **Repeated characters**: Flags same character repeated 3+ times (-1 point)

### Smart Feedback System
- Provides specific, actionable suggestions for improvement
- Only shows relevant feedback (doesn't suggest adding what's already present)
- Includes helpful password tips and best practices

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system

### Installation

1. Navigate to the project directory:
```bash
cd src/akashinferno-password-strength-checker
```

2. (Optional) Install dependencies:
```bash
pip install -r requirements.txt
```
*Note: This project uses only built-in Python libraries, so no external dependencies are required.*

### Running the Application

Simply run the main script:
```bash
python main.py
```

Or using Python 3 explicitly:
```bash
python3 main.py
```

### Usage

1. Run the script
2. Enter your password when prompted (your input will be hidden)
3. Review your password strength score and suggestions
4. Follow the recommendations to improve your password security

## 📊 Example Output

```
==================================================
🔐 PASSWORD STRENGTH CHECKER
==================================================

Enter your password (input will be hidden):
Password: 

Analyzing your password...

==================================================
RESULTS:
==================================================

Strength: 🔓 MODERATE
Score: [████████████░░░░░░░░] 6/10

📋 Suggestions to improve your password:

  💡 Consider making it longer (12+ characters is better)
  ❌ Add special characters (!@#$%^&* etc.)

==================================================

💡 Password Tips:
  • Use at least 12 characters
  • Mix uppercase, lowercase, numbers, and symbols
  • Avoid personal information (names, birthdays)
  • Don't reuse passwords across sites
  • Consider using a passphrase (e.g., 'Coffee@Morning#2025')
```

## 🎯 Password Strength Examples

| Password Example | Strength | Score | Why? |
|-----------------|----------|-------|------|
| `weak` | ⚠️ WEAK | 2/10 | Too short, no uppercase, numbers, or special chars |
| `Test123!` | 🔓 MODERATE | 6/10 | Good mix but short, has common pattern "123" |
| `MyP@ssw0rd2025!` | 🔒 STRONG | 8/10 | Long, mixed characters, special chars |

## 🛠️ Technical Details

- **Language**: Python 3
- **Dependencies**: 
  - `re` (Regular expressions - built-in)
  - `getpass` (Secure password input - built-in)
- **File Structure**:
  - `main.py` - Main application script
  - `requirements.txt` - Dependencies file (empty as only built-in libs used)
  - `README.md` - This file

## 💡 Tips for Strong Passwords

1. **Length Matters**: Aim for at least 12 characters
2. **Mix It Up**: Combine uppercase, lowercase, numbers, and symbols
3. **Avoid the Obvious**: No personal info, common words, or patterns
4. **Unique Per Site**: Don't reuse passwords across different accounts
5. **Consider Passphrases**: Easier to remember, harder to crack (e.g., "Coffee@Morning#2025!")

## 🤝 Contributing

This is a beginner-friendly project for Hacktoberfest 2025. Feel free to suggest improvements or report issues!

## 📝 License

Part of the beginner-python-mini-projects-hacktoberfest-2025 repository.

---

**Happy Secure Password Creating! 🔐**
