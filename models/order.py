from pydantic import BaseModel
from typing import List


class Order(BaseModel):
    id: int
    user_id: int
    product_ids: List[int]
    total_price: float
    status: str


orders: list[Order] = []
