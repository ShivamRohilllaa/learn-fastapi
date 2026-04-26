from fastapi import FastAPI
app = FastAPI()

from pydantic import BaseModel

from notes import services

class Notescreate(BaseModel):
    title: str
    content: str
    
class Notesupdate(BaseModel):
    id: int
    title: str
    content: str
    
    
@app.post('/create-notes')
async def notes(notes:Notescreate):
    data = await services.create_notes(title=notes.title, content=notes.content)
    return {'data': 'created'}

@app.get('/list-of-notes')
async def get_all_notes():
    data = await services.all_notes()
    return data
    
@app.put('/update-notes/{note_id}')
async def notes_update_by_id(notes:Notescreate, note_id=int):
    updated = await services.update_notes(note_id=note_id, new_title=notes.title, new_content=notes.content)
    
    if not updated:
        return {
            'error': 'not found'
        }
        
    return {'data': updated}
