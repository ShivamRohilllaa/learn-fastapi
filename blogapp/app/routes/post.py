from fastapi import APIRouter, Depends
from services.post_service import create_post, get_all_posts, get_posts_by_user_id
from schemas.post import PostCreate, PostUpdate, PostOut
from sqlalchemy.ext.asyncio import AsyncSession
from api.deps import get_db


router = APIRouter(prefix='/posts', tags=['posts'])

@router.post('/')
async def post_create(data:PostCreate, db:AsyncSession = Depends(get_db)):
    return await create_post(db, data)

@router.get('/all-post')
async def get_all(db:AsyncSession=Depends(get_db)):
    return await get_all_posts(db)
    
@router.get('/user-posts/{user_id}')
async def get_user_posts(user_id:int, db:AsyncSession=Depends(get_db)):
    return await get_posts_by_user_id(db, user_id)