from fastapi import FastAPI
from router import user, login, blogs
import model
from database import engine

fastapi = FastAPI()

model.Base.metadata.create_all(engine)

fastapi.include_router(user.router)
fastapi.include_router(login.router)
fastapi.include_router(blogs.router)

#This is one branch