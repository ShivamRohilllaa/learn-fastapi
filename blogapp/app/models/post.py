from typing import List
from sqlalchemy import ForeignKey, String, null
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base

class Post(Base):
    __tablename__ = 'post'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship('User', back_populates='posts')
    content: Mapped[str] = mapped_column(String)
    
    
    def __repr__(self):
        return f'{self.name}'
    
    
    