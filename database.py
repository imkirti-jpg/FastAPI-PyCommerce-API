from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

database_url = 'postgresql+psycopg2://postgres:postgres@localhost:5432/ecommerce_db'

engine = create_engine(database_url)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)