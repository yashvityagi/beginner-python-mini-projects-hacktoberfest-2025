import pytest

from converter import binary_to_decimal


def test_binary_to_decimal_basic():
    assert binary_to_decimal('0') == 0
    assert binary_to_decimal('1') == 1
    assert binary_to_decimal('10') == 2
    assert binary_to_decimal('1011') == 11


def test_binary_with_spaces():
    assert binary_to_decimal(' 1011 ') == 11


def test_invalid_inputs():
    with pytest.raises(ValueError):
        binary_to_decimal('')
    with pytest.raises(ValueError):
        binary_to_decimal('102')
    with pytest.raises(ValueError):
        binary_to_decimal('abc')
