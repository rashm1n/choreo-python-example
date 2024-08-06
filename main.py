from fastapi import FastAPI
from api import menu, orders, product

app = FastAPI(title="Pizzashak API")

app.include_router(menu.router)
app.include_router(orders.router)
app.include_router(product.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Pizzashak API"}