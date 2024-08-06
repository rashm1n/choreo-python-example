from fastapi import FastAPI
from api import menu, orders, product

app = FastAPI(title="Pizzashak API")

app.include_router(menu.router, prefix="/api", tags=["menu"])
app.include_router(orders.router, prefix="/api", tags=["orders"])
app.include_router(product.router, prefix="/api", tags=["products"])

@app.get("/")
async def root():
    return {"message": "Welcome to Pizzashak API"}