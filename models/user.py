from typing import List
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


users: List[User] = []