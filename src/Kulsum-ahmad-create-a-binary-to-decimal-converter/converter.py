"""
Binary to Decimal Converter
This script takes a binary input and converts it to its decimal equivalent."""


def binary_to_decimal(binary_str):
    """
    Converts a binary string to its decimal equivalent.

    Args:
        binary_str (str): A string representing a binary number.

    Returns:
        int or str: Decimal value or error message if input is invalid.
    """
    try:
        return int(binary_str, 2)
    except ValueError:
        return "Invalid binary number"


if __name__ == "__main__":
    binary_input = input("Enter a binary number: ")
    result = binary_to_decimal(binary_input)
    print(f"Decimal value: {result}")
