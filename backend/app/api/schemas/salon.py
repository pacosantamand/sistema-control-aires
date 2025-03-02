from pydantic import BaseModel
from typing import List

class SalonBase(BaseModel):
    nombre: str

class SalonCreate(SalonBase):
    edificio_id: int

class SalonUpdate(SalonBase):
    edificio_id: int

class SalonResponse(SalonBase):
    id: int
    class Config:
        from_attributes = True