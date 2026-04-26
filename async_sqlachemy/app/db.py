from sqlalchemy.ext.asyncio import create_async_engine

db_url = 'sqlite+aiosqlite:///./sqlitedb'

engine = create_async_engine(db_url, echo=True)