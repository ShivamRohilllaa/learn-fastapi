from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.deps import get_db
from schemas.user import *
from services import user_service

router = APIRouter(prefix='/user', tags=['Users'])

@router.post('/')
async def create_user(data:UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_service.create_user(db, data)