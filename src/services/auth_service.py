from src.schemas.schemas import UserCreate
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.user import User
from src.services.security_service import hash_password, verify_password

def user_signup(db: Session, user: UserCreate):
 
    user_exisit = db.query(User).filter(User.email == user.email).first()
    if user_exisit:
        raise HTTPException(status_code=400, detail= "Email Already registered")
    hashed_password = hash_password(user.password)
    new_user = User(first_name= user.first_name, last_name=user.last_name, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, email: str, password: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if user and verify_password(password, user.password_hash):
        return user
    return None
    
    