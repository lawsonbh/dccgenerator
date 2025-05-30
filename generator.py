from pydantic import BaseModel
from typing import List, Optional
import random
from roller import roll

class Character(BaseModel):
    strength: int
    agility: int
    stamina: int
    personality: int
    intelligence: int
    luck: int
    hp: int
    occupation: str
    equipment: List[str]
    alignment: str
    lucky_sign: Optional[str] = None

def generate_character() -> Character:
    # Roll stats (3d6 each)
    strength = roll("3d6")
    agility = roll("3d6")
    stamina = roll("3d6")
    personality = roll("3d6")
    intelligence = roll("3d6")
    luck = roll("3d6")
    hp = max(roll("1d4") + stamina,1) # HP Can't Be Less Than 1
    ##TODO: Add more occupations
    occupations = ["Rat Catcher", "Thief", "Merchant", "Soldier", "Farmer"]
    occupation = random.choice(occupations)
    ##TODO: Add more equipment
    equipment_map = {
        "Rat Catcher": ["Net", "Club", "1d4 copper pieces"],
        "Thief": ["Dagger","Lockpicks","1d6 silver pieces"],
        "Merchant": ["Ledger","Coin purse", "1d10 gold pieces"],
        "Soldier": ["Sword","Shield","Chainmail"],
        "Farmer": ["Pitchfork", "Sack of grain", "1d6 copper pieces"]
    }
    equipment = equipment_map.get(occupation, [])
    alignments = ["Lawful", "Neutral", "Chaotic"]
    alignment = random.choice(alignments)
    lucky_signs = [
        "Raised by Wolves (+1 Survival)",
        "Born under a Falling Star (+1 to Luck)",
        "Scarred Veteran (+1 to Melee Attacks)",
        None,
    ]
    lucky_sign = random.choice(lucky_signs)

    return Character(
        strength = strength,
        agility = agility,
        stamina = stamina,
        personality = personality,
        intelligence = intelligence,
        luck = luck,
        hp = hp,
        occupation = occupation,
        equipment = equipment,
        alignment = alignment,
        lucky_sign = lucky_sign
    )
