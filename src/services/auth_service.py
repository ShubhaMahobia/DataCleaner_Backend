from src.schemas.schemas import UserCreate
from sqlalchemy.orm import Session
from src.models.user import User

def user_signup(db: Session, user: UserCreate):
    new_user = User(first_name= user.first_name, last_name=user.last_name, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

    
    