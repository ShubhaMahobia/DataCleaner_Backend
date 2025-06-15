from src.config.db import engine, Base
from src.models.user import User

def create_tables():
    Base.metadata.create_all(bind = engine)