from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    age: int
    is_active: bool
    