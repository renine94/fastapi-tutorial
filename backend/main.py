from fastapi import FastAPI

from core.config import settings
from db.base import Base
from db.session import engine
from apis.base import api_router
from webapps.base import api_router as webapp_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)
    app.include_router(webapp_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello world!"}
