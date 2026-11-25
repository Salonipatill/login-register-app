import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# connection.py is inside backend/database, so go up to backend.
backend_dir = Path(__file__).resolve().parent.parent
load_dotenv(backend_dir / ".env")

db_password = os.getenv("DB_PASSWORD")
if not db_password:
    raise RuntimeError("DB_PASSWORD is missing. Check backend/.env.")

database_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password=db_password,
    host="localhost",
    port=3306,
    database="registration_db",
)

engine = create_engine(database_url, pool_pre_ping=True)

Sessionmaker = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()


def get_db():
    db = Sessionmaker()
    try:
        yield db
    finally:
        db.close()