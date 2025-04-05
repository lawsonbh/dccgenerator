import pytest
from roller import roll

@pytest.mark.parametrize("dice_str, min_val, max_val", [
    ("d4",1,4),
    ("1d6",1,6),
    ("2d4",2,8),
    ("3d8",3,24),
    ("4d12",4,48)
])
def test_basic_roll(dice_str, min_val, max_val):
    for _ in range(10):
        result = roll(dice_str)
        assert min_val <= result <= max_val

@pytest.mark.parametrize("dice_str, min_val, max_val", [
    ("2d6+3",5,15),
    ("1d7-2",1,5)
])
def test_with_modifiers(dice_str, min_val, max_val):
    for _ in range(10):
        result = roll(dice_str)
        assert min_val <= result <= max_val

@pytest.mark.parametrize("invalid_str", [
    "woops",
    "3d",
    "3x6",
    "d6*2"
])
def test_invalid_input(invalid_str):
    with pytest.raises(ValueError):
        roll(invalid_str)