from pydantic import BaseModel
from typing import List
from salon import SalonResponse

class EdificioBase(BaseModel):
    nombre: str

class EdificioCreate(EdificioBase):
    pass

class EdificioResponse(EdificioBase):
    id: int
    salones: List[SalonResponse] = []
    class Config:
        from_attributes = True