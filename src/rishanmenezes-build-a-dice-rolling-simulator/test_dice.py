import pytest
from dice import roll_die, roll_multiple


def test_roll_die_default():
    """Test rolling a standard 6-sided die."""
    for _ in range(10):  # Roll multiple times to check range
        result = roll_die()
        assert 1 <= result <= 6


def test_roll_die_custom():
    """Test rolling dice with different numbers of sides."""
    for sides in [4, 8, 20]:
        result = roll_die(sides)
        assert 1 <= result <= sides


def test_roll_multiple():
    """Test rolling multiple dice."""
    results = roll_multiple(3, 6)
    assert len(results) == 3
    assert all(1 <= x <= 6 for x in results)


def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        roll_die(1)  # Too few sides
    
    with pytest.raises(ValueError):
        roll_multiple(0, 6)  # Too few dice
    
    with pytest.raises(ValueError):
        roll_multiple(2, 1)  # Too few sides