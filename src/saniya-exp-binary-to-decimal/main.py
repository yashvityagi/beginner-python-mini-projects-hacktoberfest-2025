def binary_to_decimal(binary_str):
    """
    Converts a binary number (string) into its decimal equivalent.
    Example: '1010' -> 10
    """
    try:
        # int(binary_str, 2) converts binary to decimal
        decimal = int(binary_str, 2)
        return decimal
    except ValueError:
        # Raised if input is not a valid binary number
        return None


def main():
    print("💡 Welcome to the Binary to Decimal Converter 💡")
    binary_input = input("Enter a binary number (only 0s and 1s): ")

    # Convert binary to decimal
    result = binary_to_decimal(binary_input)

    if result is not None:
        print(f"The decimal value of {binary_input} is: {result}")
    else:
        print("❌ Invalid input! Please enter only binary digits (0 or 1).")


if __name__ == "__main__":
    main()
