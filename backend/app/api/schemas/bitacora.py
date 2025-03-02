from datetime import datetime
from pydantic import BaseModel
from app.api.models.bitacora import Accion
from app.api.schemas.usuario import UsuarioResponse
from app.api.schemas.aire import AireResponse

class BitacoraBase(BaseModel):
    razon: str
    accion: Accion

class BitacoraCreate(BitacoraBase):
    aire_id: int
    usuario_id: int
    
class BitacoraResponse(BitacoraBase):
    id: int
    fecha: datetime
    usuario: UsuarioResponse
    aire: AireResponse
    class Config:
        from_attributes = True