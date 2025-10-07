from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

database_url =  os.getenv("DATABASE_URL", "postgresql://ecommerce_db_b4oh_user:hQgjw6FkluvwalPZyGryZuRU40DbmV39@dpg-d3ig16s9c44c73aovpf0-a.singapore-postgres.render.com/ecommerce_db_b4oh")

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