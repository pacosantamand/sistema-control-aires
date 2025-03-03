from pydantic import BaseModel
from typing import List
from app.api.schemas.aire import AireResponse
#from app.api.schemas.edificio import EdificioResponse

class SalonBase(BaseModel):
    nombre: str

class SalonCreate(SalonBase):
    edificio_id: int

class SalonUpdate(SalonBase):
    edificio_id: int

class SalonResponse(SalonBase):
    id: int
    edificio_id: int
    #edificio: EdificioResponse
    aires: List[AireResponse] = []
    class Config:
        from_attributes = True