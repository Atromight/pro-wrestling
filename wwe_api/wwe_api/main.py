from typing import Optional

from contextlib import asynccontextmanager
from fastapi import FastAPI

from wwe_api.db import Base, engine
from wwe_api.routers import  nicknames_router, wrestlers_router
from wwe_api.loader import load_all_csv_data


@asynccontextmanager
async def db_init(app: FastAPI):
    # Startup
    print("Creating tables and loading data...")
    Base.metadata.create_all(bind=engine)
    load_all_csv_data()
    yield
    # Shutdown
    print("Shutting down...")

app = FastAPI(
    lifespan=db_init
)

@app.get("/")
async def welcome():
    return{"message": "THEN, NOW, FOREVER, TOGETHER!"}

app.include_router(nicknames_router)
app.include_router(wrestlers_router)
