import datetime
from src.config.db import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String, unique = True)
    password = Column(String)
    account_active = Column(Boolean, default = True)
    subscription_type = Column(Integer)
    created_at = Column(DateTime, default = datetime.datetime.now())
    updated_at = Column(DateTime, default = datetime.datetime.now())