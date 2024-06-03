from typing import List  # Add this import statement

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import controller, schemas, database

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/users/", response_model=List[schemas.User])
def get_users(db: Session = Depends(database.get_db)):
    users = controller.get_users(db)
    return users

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = controller.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = controller.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return controller.create_user(db=db, user=user)