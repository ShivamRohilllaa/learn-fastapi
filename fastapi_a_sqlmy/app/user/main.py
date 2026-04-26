from fastapi import FastAPI
from user.services import create_user, get_all_users
from pydantic import BaseModel

app = FastAPI()


class CreateUser(BaseModel):
    name: str
    
@app.post('/create-user')
async def create_user(user:CreateUser):
    data = await create_user(name=user.name)
    return {'data': data}

@app.get('/all-users')
async def get_all_users():
    data = await get_all_users()
    return data