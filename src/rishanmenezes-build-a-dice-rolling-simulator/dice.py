"""Dice rolling utilities."""

from random import randint
from typing import List


def roll_die(sides: int = 6) -> int:
    """Roll a single die with the given number of sides (default 6).
    
    Args:
        sides: Number of sides on the die (must be >= 2)
    
    Returns:
        Random number between 1 and sides (inclusive)
        
    Raises:
        ValueError: If sides < 2
    """
    if sides < 2:
        raise ValueError("Die must have at least 2 sides")
    return randint(1, sides)


def roll_multiple(num: int = 1, sides: int = 6) -> List[int]:
    """Roll multiple dice and return their results.
    
    Args:
        num: Number of dice to roll (must be >= 1)
        sides: Number of sides per die (must be >= 2)
        
    Returns:
        List of random numbers, each between 1 and sides
        
    Raises:
        ValueError: If num < 1 or sides < 2
    """
    if num < 1:
        raise ValueError("Must roll at least one die")
    return [roll_die(sides) for _ in range(num)]