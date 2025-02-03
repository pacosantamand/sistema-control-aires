from pydantic import BaseModel
from typing import List
from horario import HorarioResponse

class AireBase(BaseModel):
    nombre: str
    estado: bool

class AireCreate(AireBase):
    salon_id: int

class AireResponse(AireBase):
    id: int
    horarios: List[HorarioResponse] = []
    class Config:
        from_attributes = True