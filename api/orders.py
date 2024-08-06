from fastapi import APIRouter, HTTPException
from models.order import Order, orders
from models.user import users
from models.product import products
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/orders")
async def get_orders():
    logger.info("Fetching all orders")
    return orders


@router.post("/orders/", response_model=Order)
async def create_order(order: Order):
    logger.info(f"Creating order for user: {order.user_id}")
    if not any(u.id == order.user_id for u in users):
        logger.error(f"User with id {order.user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")

    total_price = 0
    for product_id in order.product_ids:
        product = next((p for p in products if p.id == product_id), None)
        if not product:
            logger.error(f"Product with id {product_id} not found")
            raise HTTPException(status_code=404, detail="Product not found")
        if product.stock <= 0:
            logger.warning(f"Product {product.name} is out of stock")
            raise HTTPException(status_code=400, detail=f"Product {product.name} is out of stock")
        total_price += product.price
        product.stock -= 1

    order.total_price = total_price
    order.status = "Pending"
    orders.append(order)
    logger.info(f"Order {order.id} created successfully")
    return order


@router.get("/orders/{order_id}")
async def get_order(order_id: int):
    logger.info(f"Fetching order with id: {order_id}")
    order = next((order for order in orders if order.id == order_id), None)
    if order is None:
        logger.warning(f"Order not found: {order_id}")
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/orders/{order_id}")
async def update_order(order_id: int, updated_order: Order):
    logger.info(f"Updating order with id: {order_id}")
    for i, order in enumerate(orders):
        if order.id == order_id:
            updated_order.id = order_id
            orders[i] = updated_order
            return updated_order
    logger.warning(f"Order not found for update: {order_id}")
    raise HTTPException(status_code=404, detail="Order not found")
