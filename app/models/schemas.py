from pydantic import BaseModel
from typing import List

class UserRequest(BaseModel):
    domains: List[str]
    difficulty: int

class GeneratedResponse(BaseModel):
    question: str
    difficulty: int
    domains: List[str]
