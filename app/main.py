from typing import Annotated
from fastapi import FastAPI, Form, Request

app = FastAPI()

from pydantic import BaseModel, ValidationError

@app.middleware('http')
async def first_middleware(request:Request, call_next):
    print(
        'first_call'
    )
    response = await call_next(request)
    print('final call')
    return response

class UserCreate(BaseModel):
    name: str
    age: int
    is_active: bool
    
#show only necessary data so for that we will use responsemodel
class UserData(BaseModel):
    name: str
    age: int
    
    
@app.get('/')
def home():
    return {'msg': 'This is my first fastapi project'}

@app.get('/users')
def get_users():
    return {'users_data': ['Shivam', 'Raj', 'Ram']}

@app.post('/create_users')
def create_users():
    return {'msg': 'User created successfully'}

@app.get('/list_users_async')
async def list_of_users():
    return {'user_lists': ['Shivam', 'Raj', 'Ram']}

#This is path parameter
@app.get('/users/{user_id}')
async def get_user_data(user_id:int):
    return {'user_data':f'User id is {user_id}'}

#This is query parameter
@app.get('/search')
async def search(q:str = None):
    return {'search_res':f'search query is {q}'}

#combine the both path and query parameter
@app.get('/product_list/{cat_id}')
async def product_list(cat_id:int, q:str=None):
    return {'product_list':f'Category id is {cat_id} and search query is {q}'}

@app.post('/users')
async def create_user_data(user: UserCreate):
    return {'data': user}

@app.get('/product/{product_id}')
async def get_products_by_id(product_id:int):
    return {'data': f'product is {product_id}'}

@app.post('/users-reponse', response_model=UserData)
async def get_user_data_response(user: UserCreate):
    return user


#how to pass form data
@app.post('/login')
async def get_login(username: Annotated[str, Form(min_length=2, max_length=20)], password: Annotated[str, Form(min_length=8, max_length=20)]):
    return {username, password}

@app.middleware('http')
async def first_middleware(request:Request, call_next):
    print(
        'first_call'
    )
    response = await call_next(request)
    print('final call')
    return response
    