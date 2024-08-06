from fastapi import APIRouter, HTTPException
from models.product import Product, products
import logging


router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/products/", response_model=Product)
async def create_product(product: Product):
    logger.info(f"Creating product: {product.name}")
    if any(p.id == product.id for p in products):
        logger.warning(f"Product with id {product.id} already exists")
        raise HTTPException(status_code=400, detail="Product already exists")
    products.append(product)
    return product

@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    logger.info(f"Fetching product with id: {product_id}")
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        logger.error(f"Product with id {product_id} not found")
        raise HTTPException(status_code=404, detail="Product not found")
    return product