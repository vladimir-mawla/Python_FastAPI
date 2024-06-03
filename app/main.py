from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import controller, schemas, database, auth

app = FastAPI()

app.include_router(auth.router)

@app.get("/", summary="Root endpoint", tags=["Root"])
def read_root():
    """Root endpoint returning a simple message."""
    return {"message": "Hello, World!"}

@app.get("/users/", response_model=List[schemas.User], summary="Get all users", tags=["Users"])
def get_users(db: Session = Depends(database.get_db)):
    """Get all users."""
    users = controller.get_users(db)
    return users

@app.post("/users/", response_model=schemas.User, summary="Create a new user", tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """Create a new user."""
    db_user = controller.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = controller.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return controller.create_user(db=db, user=user)