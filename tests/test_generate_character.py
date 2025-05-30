import pytest
from generator import generate_character, Character

def test_generate_character_basic():
    char = generate_character()

    # Check Type
    assert isinstance(char, Character)

    # All stats should be between 3 and 18 (3d6 roll)
    for stat in ['strength', 'agility', 'stamina', 'personality', 'intelligence', 'luck']:
        value = getattr(char,stat)
        assert 3 <= value <= 18, f"{stat} out of range: {value}"
    
    # HP must be greater than 0
    assert char.hp > 0