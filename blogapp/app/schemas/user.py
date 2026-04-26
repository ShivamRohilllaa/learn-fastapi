from typing import Optional
from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    email:str
    
class UserOut(BaseModel):
    id:int
    name:str
    email:str
    
class Userupdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None