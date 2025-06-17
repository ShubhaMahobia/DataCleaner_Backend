from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import UserCreate
from src.config.db import get_db
from src.services.auth_service import user_signup


auth_router = APIRouter(prefix="/users-auth", tags=["users-auth"])

@auth_router.post("/signup")
async def user_signup_api(user: UserCreate, db: Session = Depends(get_db)):
    return user_signup(db, user)