from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .routers import *
from .db.init_db import init_db

init_db()

app = FastAPI()

app.include_router(item.router, prefix="/graphql")