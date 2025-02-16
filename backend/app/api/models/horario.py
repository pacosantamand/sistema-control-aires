from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dia = Column(String(15), nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    aire_id = Column(Integer, ForeignKey("aires_acondicionados.id"))

    aire = relationship("AireAcondicionado", back_populates="horarios")