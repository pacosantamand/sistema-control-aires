from pydantic import BaseModel, Field, field_validator
from datetime import time

class HorarioBase(BaseModel):
    dia: str = Field(..., example="Lunes")
    hora_inicio: time = Field(..., example="08:00:00")
    hora_fin: time = Field(..., example="18:00:00")
    @field_validator("hora_fin")
    @classmethod
    def validar_horario(cls, hora_fin, values):
        """Validar que la hora de inicio sea menor que la hora de fin"""
        hora_inicio = values.data.get("hora_inicio")
        if hora_inicio and hora_fin <= hora_inicio:
            raise ValueError("La hora de inicio debe ser menor que la hora de fin")
        return hora_fin
    
class HorarioCreate(HorarioBase):
    aire_id: int

class HorarioUpdate(HorarioBase):
    aire_id: int
    
class HorarioResponse(HorarioBase):
    id: int
    class Config:
        from_attributes = True