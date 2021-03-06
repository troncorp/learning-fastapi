from async_apis.schemas import Article
from fastapi import FastAPI
from .db import database
from . import articles,users,auth

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(articles.router)
app.include_router(users.router)
app.include_router(auth.router)