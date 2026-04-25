from fastapi import FastAPI, HTTPException

app = FastAPI()

data ={
    'apple': 'red',
    'mango': 'yellow'
}

@app.get('/product/{product_id}')
async def get_fruit(product_id: str):
    if product_id not in data:
        raise HTTPException(status_code=404, detail='Item not found')
    return data[product_id]


#Adding custom header for logging in the api
@app.get('/items/{item_id}')
async def get_items(item_id: str):
    if item_id not in data:
        raise HTTPException(status_code=404, detail='Not found', headers={'x-error-type': 'item not found'})
    