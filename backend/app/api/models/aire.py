from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class AireAcondicionado(Base):
    __tablename__ = "aires_acondicionados"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), index=True, unique=True)
    estado = Column(Boolean, default=False) 
    salon_id = Column(Integer, ForeignKey("salones.id")) 

    horarios = relationship("Horario", back_populates="aire")
    salon = relationship("Salon", back_populates="aires")
    bitacora = relationship("Bitacora", back_populates="aire")