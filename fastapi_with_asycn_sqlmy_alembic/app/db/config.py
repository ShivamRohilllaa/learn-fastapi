from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "sqlite.db")

db_url ='sqlite+aiosqlite:///{db_path}'

engine = create_async_engine(db_url, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)