"""Simple binary to decimal conversion utilities.

Beginner-friendly implementation.
"""

def binary_to_decimal(binary_str: str) -> int:
    """Convert a binary string (e.g. '1011') to decimal.

    Strips surrounding whitespace. Raises ValueError for invalid input.
    """
    if not isinstance(binary_str, str):
        raise ValueError("Input must be a string containing only 0 and 1")

    s = binary_str.strip()
    if s == "":
        raise ValueError("Empty input is not a valid binary number")

    if any(ch not in "01" for ch in s):
        raise ValueError("Invalid binary number: only characters '0' and '1' are allowed")

    return int(s, 2)
