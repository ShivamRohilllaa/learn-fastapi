from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base
# from user.models import User

class Product(Base):
    __tablename__ = 'products'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    # user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    # user: Mapped['User'] = relationship('User', back_populates='product')
    
    def __repr__(self):
        return f'{self.name}'
    
    