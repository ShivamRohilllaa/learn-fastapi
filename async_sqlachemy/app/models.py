from sqlalchemy import Column, Integer, MetaData, String, Table
from db import engine

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(length=50), nullable=False)
)