from pydantic import BaseModel
from datetime import time

class HorarioBase(BaseModel):
    dia: str
    hora_inicio: time
    hora_fin: time

class HorarioCreate(HorarioBase):
    aire_id: int

class HorarioUpdate(HorarioBase):
    aire_id: int
    
class HorarioResponse(HorarioBase):
    id: int
    class Config:
        from_attributes = True