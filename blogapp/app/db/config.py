from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(BASE_DIR)
db_path = os.path.join(APP_DIR, "sqlite.db")

db_url = f"sqlite+aiosqlite:///{db_path}"

engine = create_async_engine(db_url, echo=True)

localsession = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
