from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Salon(Base):
    __tablename__ = "salones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)

    edificio = relationship("Edificio", back_populates="salon")
    aires = relationship("AireAcondicionado", back_populates="salon")