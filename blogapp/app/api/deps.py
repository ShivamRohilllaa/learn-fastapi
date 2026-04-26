from db.config import localsession

async def get_db():
    async with localsession() as session:
        yield session