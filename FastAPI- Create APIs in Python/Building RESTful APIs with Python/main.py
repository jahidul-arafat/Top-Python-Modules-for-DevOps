from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        #id=uuid4(),
        id=UUID("56c459e5-7c25-4110-baa9-7a0885ca7ab1"),
        first_name="Jahidul",
        last_name="Arafat",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        #id=uuid4(),
        id=UUID("d9319040-956d-4ed4-9cd8-0bab2d5a4969"),
        first_name="Fariha",
        last_name="Tasmin",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )
]

#The root path
@app.get("/")
async def root():
    return {"Hello": "Oracle"}

#Get the list of all existing users
@app.get("/api/v1/users")
async def fetch_users():
    return db;

#Register a new user
@app.post("/api/v1/users")
async def register_user(user:User):
    db.append(user)
    return {"id": user.id}

#Delete a user
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )

#Update a user
@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id : {user_id} does not exists"
    )
