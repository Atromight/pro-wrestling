from typing import Optional

from fastapi import FastAPI

from wwe_api.routers.wrestlers import wrestlers_router

app = FastAPI()

@app.get("/")
async def welcome():
    return{"message": "THEN, NOW, FOREVER, TOGETHER!"}

app.include_router(wrestlers_router)
