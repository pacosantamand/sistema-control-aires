import enum 
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship 
from app.database import Base


class Rol(enum.Enum):
    colaborador = "colaborador"
    administrador = "administrador"


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50))
    email = Column(String(100), index = True, unique = True)
    password = Column(String(100))
    rol = Column(Enum(Rol))

    bitacora = relationship("Bitacora", back_populates="usuario")