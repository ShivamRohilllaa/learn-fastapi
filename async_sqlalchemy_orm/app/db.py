from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


db_url = 'sqlite+aiosqlite:///sqlite.db'

engine = create_async_engine(db_url, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
