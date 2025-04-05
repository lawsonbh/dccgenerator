import re
import random

dice_regexp = re.compile(r'(\d*)d(\d+)([+-]\d+)?')

def roll(dice_str: str) -> int:
    match = dice_regexp.fullmatch(dice_str.lower().strip())
    if not match:
        raise ValueError(f"Invalid Dice String: {dice_str} must be like '1d6-1'")

    # Saying d6 is equivalent to saying 1d6
    num = int(match.group(1)) if match.group(1) else 1
    
    # Different kinds of dice on the chain, 2,3,4,5,6,7,8,9,etc.
    sides = int(match.group(2))

    # Absolute modifier to add or'(\d*)d(\d+)([+-]\d+)?'r subtract from roll result
    modifier = int(match.group(3)) if match.group(3) else 0

    total = max(sum(random.randint(1, sides) for _ in range(num)) + modifier,1)
    return total