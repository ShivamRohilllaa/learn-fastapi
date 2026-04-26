from fastapi import FastAPI
from user import services
from pydantic import BaseModel
from product import services as prod_services

app = FastAPI()


class CreateUser(BaseModel):
    name: str
    
class Createproduct(BaseModel):
    name:str
        
@app.post('/create-user')
async def user_create(user:CreateUser):
    await services.create_user(name=user.name)
    return {'data': 'user created'}

@app.get('/all-users')
async def get_all_users():
    data = await services.get_all_users()
    return data

@app.post('/create-product')
async def create_product(product:Createproduct):
    await prod_services.create_product(name=product.name)
    return {'data': 'created'}

@app.get('/all-products')
async def get_all_products():
    data = await prod_services.get_all_prod()
    return data