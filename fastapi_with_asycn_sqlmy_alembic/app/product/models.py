from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db.base import Base

class Product(Base):
    __tablename__ = 'products'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    
    def __repr__(self):
        return f'{self.name}'
    