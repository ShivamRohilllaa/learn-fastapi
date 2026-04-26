from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.post import Post


async def create_post(db:AsyncSession, data):
    post = Post(**data.dict())
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post

async def get_post_by_id(db:AsyncSession, post_id:int):
    stmt = await db.get(Post, post_id)
    return stmt

async def update_post_by_id(db:AsyncSession, post_id:int, new_title:str, new_content:str):
    stmt = await db.get(Post, post_id)
    if stmt:
        stmt.title = new_title
        stmt.content = new_content
        await db.commit()
        await db.refresh(stmt)
        return stmt

async def get_posts_by_user_id(db:AsyncSession, user_id:int):
    stmt = await db.execute(select(Post).where(Post.user_id==user_id))
    data = stmt.scalars().all()
    return data
    
async def get_all_posts(db:AsyncSession):
    data = await db.execute(select(Post))
    return data.scalars().all()