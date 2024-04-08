from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#create engine
engine = create_engine("sqlite:///./database.db", connect_args={"check_same_thread": False})
#create base model
Base = declarative_base()
#create sessions in database
SessionLocal = sessionmaker(bind = engine, autoflush= False, autocommit = False)

def get_db():
    db = SessionLocal()
    try: 
        return db
    finally: 
        db.close()