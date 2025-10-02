"""Small interactive CLI for the binary-to-decimal converter."""

from .converter import binary_to_decimal


def main() -> None:
    print("Binary to Decimal Converter (type 'exit' to quit)")
    try:
        while True:
            inp = input("Enter a binary number: ").strip()
            if inp.lower() in {"exit", "quit"}:
                print("Goodbye!")
                break
            try:
                dec = binary_to_decimal(inp)
                print(f"Decimal: {dec}")
            except ValueError as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
