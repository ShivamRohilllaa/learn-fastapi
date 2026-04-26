from fastapi import FastAPI
from routes import user, post

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)