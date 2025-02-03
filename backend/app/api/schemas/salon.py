from pydantic import BaseModel
from typing import List
from aire import AireResponse

class SalonBase(BaseModel):
    nombre: str

class SalonCreate(SalonBase):
    pass

class SalonResponse(SalonBase):
    id: int
    aires: List[AireResponse] = []
    class Config:
        from_attributes = True