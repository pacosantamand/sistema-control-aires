import enum, datetime
from sqlalchemy import Column, ForeignKey, Integer, Text, Enum, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Accion(enum.Enum):
    encender = "encender"
    apagar = "apagar"

class Bitacora(Base):
    __tablename__ = "bitacora"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    razon = Column(Text)
    accion = Column(Enum(Accion))
    fecha = Column(DateTime,  default=datetime.datetime.now)
    aire_id = Column(Integer, ForeignKey("aires_acondicionados.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    aire = relationship("AireAcondicionado", back_populates="bitacora")
    usuario = relationship("Usuario", back_populates="bitacora")
