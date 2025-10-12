"""Interactive CLI for the simple calculator project."""

from calculator import add, subtract, multiply, divide, power

OPERATIONS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
    "5": ("Power", power),
}

def prompt_number(prompt: str):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Simple Calculator — safwanahmadsaffi")
    while True:
        print("\nSelect operation:")
        for k, (name, _) in OPERATIONS.items():
            print(f"  {k}. {name}")
        print("  q. Quit")

        choice = input("Choice: ").strip()
        if choice.lower() == "q":
            print("Goodbye.")
            break

        if choice not in OPERATIONS:
            print("Invalid choice, try again.")
            continue

        a = prompt_number("Enter first number: ")
        b = prompt_number("Enter second number: ")

        _, func = OPERATIONS[choice]
        try:
            result = func(a, b)
        except Exception as e:
            print(f"Error: {e}")
        else:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()
