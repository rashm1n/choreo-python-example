from pydantic import BaseModel


class MenuItem(BaseModel):
    id: int = None
    name: str
    description: str
    price: float


menu_items: list[MenuItem] = []
