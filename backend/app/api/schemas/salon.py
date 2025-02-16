from pydantic import BaseModel
from typing import List
from app.api.schemas.aire import AireResponse

class SalonBase(BaseModel):
    nombre: str

class SalonCreate(SalonBase):
    edificio_id: int

class SalonUpdate(SalonBase):
    edificio_id: int

class SalonResponse(SalonBase):
    id: int
    aires: List[AireResponse] = []
    class Config:
        from_attributes = True