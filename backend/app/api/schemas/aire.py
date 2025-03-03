from pydantic import BaseModel
from typing import List

from app.api.schemas.horario import HorarioResponse
#from app.api.schemas.salon import SalonResponse

class AireBase(BaseModel):
    nombre: str

class AireCreate(AireBase):
    salon_id: int

class AireUpdate(AireBase):
    salon_id: int

class AireResponse(AireBase):
    id: int
    estado: bool
    #salon: SalonResponse
    salon_id: int
    horarios: List[HorarioResponse] = []

    class Config:
        from_attributes = True