from typing import List
from fastapi import FastAPI, Query
from generator import generate_character, Character

app = FastAPI()

@app.get("/generate-characters", response_model=List[Character])
def get_characters(count: int = Query(1,ge=1, le=100)):
    """
    Generate 1 or more characters.
    `count` must be between 1 and 100 (inclusive).
    """
    return [generate_character() for _ in range(count)]
