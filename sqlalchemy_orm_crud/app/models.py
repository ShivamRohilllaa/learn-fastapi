from typing import List
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from db import engine

class Base(DeclarativeBase):
    pass

#association or mapping table

user_categories = Table(
    'user_categories',
    Base.metadata,
    Column('user_id', ForeignKey('users.id', ondelete='CASCADE')),
    Column('cat_id', ForeignKey('category.id', ondelete='CASCADE'))
)

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    profile: Mapped['Profile'] = relationship('Profile', back_populates='user', cascade='all, delete-orphan')
    category: Mapped[List['Category']] = relationship('Category', back_populates='user', secondary='user_categories')
    post: Mapped[List['Post']] = relationship('Post', back_populates='user', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'{self.name}'
    
class Post(Base):
    __tablename__ = 'posts'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    user: Mapped['User'] = relationship('User', back_populates='post')
    
    def __repr__(self):
        return f'{self.title}'
    
class Profile(Base):
    __tablename__ = 'profile'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), unique=True, nullable=False)
    user: Mapped['User'] = relationship('User', back_populates='profile')
    bio: Mapped[str] = mapped_column(String(100), nullable=True)
    fullname: Mapped[str] = mapped_column(String(100), nullable=True)
    
    def __repr__(self):
        return f'{self.fullname}'
    
class Category(Base):
    __tablename__ = 'category'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    user: Mapped[List['User']] = relationship('User', back_populates='category', secondary='user_categories')
    
    def __repr__(self):
        return f'{self.title}'
    

def create_tables():
    return Base.metadata.create_all(engine)