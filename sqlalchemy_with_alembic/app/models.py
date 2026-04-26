from sqlalchemy import String, null
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=True, unique=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    
    def __repr__(self):
        return f'{self.name}'