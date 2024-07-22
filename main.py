from fastapi import FastAPI

from models import User


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


users = []

# get All Users

@app.get("/users")
async def get_users():
    return {"users": users}


# Post a  User

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"users": users}






