from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = 'sqlite:///./sqlitedb'

engine = create_engine(db_url, echo=True)

localsession = sessionmaker(bind=engine, expire_on_commit=False)