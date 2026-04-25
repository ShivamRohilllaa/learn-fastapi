from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from db import engine

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f'name:{self.name} and email is {self.email}'

class Address(Base):
    __tablename__ = 'address'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    address_opt: Mapped[str] = mapped_column(String(100), nullable=True)
    
    def __repr__(self):
        return f'address is {self.address}'
    
    
def create_tables():
    Base.metadata.create_all(engine)