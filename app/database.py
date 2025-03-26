from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from urllib.parse import quote_plus

ENCODED_PASSWORD = quote_plus(settings.DATABASE_PASSWORD)

SQLACHEMY_DATABSE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{ENCODED_PASSWORD}@{settings.DATABASE_HOST_NAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine = create_engine(SQLACHEMY_DATABSE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# DB Connection for RAW SQL
"""
import psycopg2
from psycopg2.extras import RealDictCursor
while True: 
    try:
        conn = psycopg2.connect(host ='localhost', database ='fastapi', user ='postgres', password ='Admin@123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Failed to connect")
        print("Error: ", error)
        time.sleep(2)
"""