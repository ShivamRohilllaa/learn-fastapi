from pydantic import BaseModel
from sqlalchemy import Select
from db.config import async_session
from product.models import Product

async def create_product(name:str):
    async with async_session() as session:
        data = Product(name=name)
        session.add(data)
        await session.commit()
        
async def get_all_prod():
    async with async_session() as session:
        prod = Select(Product)
        data = await session.scalars(prod)
        return data.all()