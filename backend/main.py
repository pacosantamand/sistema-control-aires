from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.database import engine, Base, SessionLocal
from app.api.routers import aire, edificio, salon, horario, usuario, websocket, bitacora
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        Base.metadata.create_all(bind=engine) 
        yield
    finally:
        engine.dispose() 



app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen (puedes restringirlo a un dominio específico)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(edificio.router)
app.include_router(salon.router)
app.include_router(aire.router)
app.include_router(horario.router)
app.include_router(usuario.router)
app.include_router(bitacora.router)

app.include_router(websocket.router)


