from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int


products: List[Product] = []
