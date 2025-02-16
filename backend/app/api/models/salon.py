from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Salon(Base):
    __tablename__ = "salones"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), unique=True, index=True)
    edificio_id = Column(Integer, ForeignKey("edificios.id"))

    edificio = relationship("Edificio", back_populates="salones")
    aires = relationship("AireAcondicionado", back_populates="salon")