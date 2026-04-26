from db.config import async_session
from sqlalchemy import Select, select
from user.models import User

async def create_user(name:str):
    async with async_session() as session:
        data = User(name=name)
        session.add(data)
        await session.commit()
        
async def get_all_users():
    async with async_session() as session:
        stmt = Select(User)
        data = await session.scalars(stmt)
        return data.all()