from typing import Optional
from pydantic import BaseModel

class PostCreate(BaseModel):
    name: str
    content: str
    user_id:int
    
class PostOut(BaseModel):
    id:int
    name:str
    content:str

class PostUpdate(BaseModel):
    name: Optional[str] = None
    content: Optional[str] = None