from fastapi import APIRouter, HTTPException
from models.menu import MenuItem, menu_items
import logging
router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/menu")
async def get_menu():
    logger.info("Fetching menu items")
    return menu_items


@router.get("/menu/{item_id}")
async def get_menu_item(item_id: int):
    logger.info(f"Fetching menu item with id: {item_id}")
    item = next((item for item in menu_items if item.id == item_id), None)
    if item is None:
        logger.warning(f"Menu item not found: {item_id}")
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/menu")
async def add_menu_item(item: MenuItem):
    logger.info(f"Adding new menu item: {item.name}")
    item.id = len(menu_items) + 1
    menu_items.append(item)
    return item


@router.put("/menu/{item_id}")
async def update_menu_item(item_id: int, updated_item: MenuItem):
    for i, item in enumerate(menu_items):
        if item.id == item_id:
            updated_item.id = item_id
            menu_items[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/menu/{item_id}")
async def delete_menu_item(item_id: int):
    for i, item in enumerate(menu_items):
        if item.id == item_id:
            return menu_items.pop(i)
    raise HTTPException(status_code=404, detail="Item not found")
