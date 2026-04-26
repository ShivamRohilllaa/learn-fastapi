from fastapi import HTTPException
from sqlalchemy import select
from db.config import localsession
from notes.models import Notes

async def create_notes(title:str, content:str):
    async with localsession() as session:
        stmt = Notes(title=title, content=content)
        session.add(stmt)
        await session.commit()
        await session.refresh(stmt)
        return stmt
        
async def all_notes():
    async with localsession() as session:
        stmt = select(Notes)
        data = await session.scalars(stmt)
        return data.all()

async def get_notes_by_id(note_id: int):
    async with localsession() as session:
        stmt = await session.get(Notes, note_id)
        if not stmt:
            raise HTTPException(status_code=404, detail='not found')
        return stmt
        
async def update_notes(note_id:int, new_title:str, new_content:str):
    async with localsession() as session:
        data = await session.get(Notes, note_id)
        if data is None:
            raise HTTPException(status_code=404, detail='not found')
        
        data.title = new_title
        data.content = new_content
        
        await session.commit()
        await session.refresh(data)
        return data
        