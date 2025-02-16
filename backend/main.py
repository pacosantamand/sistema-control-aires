from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app.api.routers import aire, edificio, salon, horario, websocket


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        Base.metadata.create_all(bind=engine) 
        yield
    finally:
        engine.dispose() 



app = FastAPI(lifespan=lifespan)

app.include_router(edificio.router)
app.include_router(salon.router)
app.include_router(aire.router)
app.include_router(horario.router)
app.include_router(websocket.router)


