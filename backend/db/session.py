from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

# PostgreSQL
# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLite
SQLALCHEMY_DATABSSE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABSSE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
