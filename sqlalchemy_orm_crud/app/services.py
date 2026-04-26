from select import select
from sqlalchemy import Select, asc
from sqlalchemy.sql.functions import user
from db import localsession
from models import Post, Profile, User, Category



def create_user(name:str, email:str):
    with localsession() as session:
        user_data = User(name=name, email=email)
        session.add(user_data)
        session.commit()
        session.refresh(user_data)
        return user_data

def create_profile(user_id: int, bio:str, fullname:str):
    with localsession() as session:
        cat = Profile(bio=bio, fullname=fullname, user_id=user_id)
        session.add(cat)
        session.commit()
        
def create_category(title:str):
    with localsession() as session:
        data = Category(title=title)
        session.add(data)
        session.commit()

def create_post(title:str, content:str, user_id:int):
    with localsession() as session:
        data = Post(title=title, content=content, user_id=user_id)
        session.add(data)
        session.commit()

def update_post(title:str, id:int):
    with localsession() as session:
        data = session.get(Post, id)
        if data:
            data.title = title
            session.commit()
            session.refresh(data)
            return data
            
        
        
#def get user by id

def get_user(user_id:int):
    with localsession() as session:
        user = session.get_one(User, user_id)
        return user
        
#get post by id

def get_post(id:int):
    with localsession() as session:
        stmt = Select(Post).where(Post.id==id)
        data = session.scalars(stmt).first()
        return data
    
#get all users

def get_all_users():
    with localsession() as session:
        stmt = Select(User).order_by(asc(User.name))
        data = session.scalars(stmt).all()
        return data