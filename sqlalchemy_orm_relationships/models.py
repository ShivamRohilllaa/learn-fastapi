from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Nullable, String, ForeignKey


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age : Mapped[int] = mapped_column(nullable=False)
    profile: Mapped['Profile'] = relationship("Profile", back_populates='user', uselist=False, cascade='all, delete')
    
    def __repr__(self):
        return f'{self.name}'
    


class Profile(Base):
    __tablename__ = 'profile'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    
    def __repr__(self):
        return self.name
    