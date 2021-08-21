from fastapi import FastAPI

from core.config import settings
from db.base import Base
from db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello world!"}
