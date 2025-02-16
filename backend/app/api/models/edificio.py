from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Edificio(Base):
    __tablename__ = "edificios"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    nombre = Column(String(50), unique=True, index=True)

    salones = relationship("Salon", back_populates="edificio")