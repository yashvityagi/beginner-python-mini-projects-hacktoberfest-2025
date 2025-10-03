import argparse
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """
    Generate a random password based on the specified criteria.
    """
    chars = ''
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character type must be selected")

    return ''.join(random.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password (default: 12)')
    parser.add_argument('--no-upper', action='store_false', dest='upper', default=True, help='Exclude uppercase letters')
    parser.add_argument('--no-lower', action='store_false', dest='lower', default=True, help='Exclude lowercase letters')
    parser.add_argument('--no-digits', action='store_false', dest='digits', default=True, help='Exclude digits')
    parser.add_argument('--no-symbols', action='store_false', dest='symbols', default=True, help='Exclude symbols')

    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.upper, args.lower, args.digits, args.symbols)
        print(password)
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    return 0

if __name__ == '__main__':
    exit(main())