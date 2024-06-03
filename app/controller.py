from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

