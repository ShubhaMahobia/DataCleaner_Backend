from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config.init_db import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan = lifespan)


@app.get('/health')
def health_check():
    return {
      "success" : True,
      "message" : "Server is running"  
    }

