from db import engine
from sqlalchemy import Boolean, Column, ForeignKey, Integer, MetaData, Nullable, String, Table, null

metadata = MetaData()

#User Table
users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(length=50), nullable=False),
    Column('email', String(length=50), nullable=False, unique=True),
    Column('phone', Integer, unique=True, nullable=False)
)

address = Table(
    'address',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('address', String(length=90), nullable=False),
    Column('address2', String, nullable=True),
    Column('state', String, nullable=False),
    Column('city', String, nullable=False),
    Column('zipcode', Integer, nullable=True)
    
)

#One to Many relation

posts = Table(
    'posts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id', on_delete='CASCADE'), nullable=False),
    Column('title', String(length=200), nullable=False),
    Column('desc', String, nullable=True),
    Column('is_published', Boolean, default=False)
)

#One to One Relation

profile = Table(
    'profile',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("users.id", on_delete='CASCADE'),unique=True, nullable=False,),
    Column('bio', String(length=500), nullable=True)
)

#For Many to Many Relation we have to create a mapping table

user_addresses = Table(
    'user_addresses',
    metadata,
    Column('user_id', Integer, ForeignKey('users.id', on_delete='CASCADE'),primary_key=True),
    Column('address_id', Integer, ForeignKey('address.id', ondelete='CASCADE'), primary_key=True)
    )

#Create tables in Database
def create_tables():
    metadata.create_all(engine)
    
#drop all tables
def drop_tables():
    metadata.drop_all(engine)