from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, MetaData, Nullable, String, ForeignKey, Table, null
from typing import List

from db import engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age : Mapped[int] = mapped_column(nullable=False)
    profile: Mapped['Profile'] = relationship("Profile", back_populates='user', uselist=False, cascade='all, delete-orphan')
    posts: Mapped[list('Posts')] = relationship('Posts', back_populates='user', cascade='all, delete-orphan')
    addresses: Mapped[list('Addresses')] = relationship('Addresses', back_populates='user')
    
    def __repr__(self):
        return f'{self.name}'
    

class Profile(Base):
    __tablename__ = 'profile'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'), nullable=False, unique=True)
    user: Mapped['User'] = relationship('User', back_populates='profile', cascade='all, delete')
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    
    def __repr__(self):
        return f'{self.name}'
    
    
class Posts(Base):
    __tablename__ = 'posts'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user: Mapped['User'] = relationship('User', back_populates='posts', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'{self.name}'
    
class Addresses(Base):
    __tablename__ = 'addresses'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    address1: Mapped[str] = mapped_column(String(150), nullable=False)
    address2: Mapped[str] = mapped_column(String, nullable=True)
    user: Mapped['User'] = relationship('User', back_populates='address')
    
    
    def __repr__(self):
        return f'{self.name}'
    

user_addresses = Table(
    'user_address_mapping',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE')),
    Column('address_id', Integer, ForeignKey('addresses.id', ondelete='CASCADE'))
)
    
def create_tables():
    return Base.metadata.create_all(engine)