from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Si se utiliza SQLite
#SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db" 
#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#Si se utiliza MySql se debe deshabilitar 
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://devs:password@localhost/horarios_aire"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()