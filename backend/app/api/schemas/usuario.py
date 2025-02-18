from pydantic import BaseModel
from app.api.models.usuario import Rol

class UsuarioBase(BaseModel):
    nombre: str
    email: str
    rol: Rol

class UsuarioCreate(UsuarioBase):
    password: str
    
class UsuarioUpdate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: int
