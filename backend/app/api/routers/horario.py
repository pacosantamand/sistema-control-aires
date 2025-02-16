from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.api.models.horario import Horario
from app.api.schemas.horario import HorarioCreate, HorarioUpdate, HorarioResponse
from typing import List

router = APIRouter(prefix="/horarios", tags=["horarios"])

@router.post("/", response_model=HorarioResponse)
def crear_horario(horario: HorarioCreate, db: Session = Depends(get_db)):
    nuevo_horario = horario(**horario.model_dump())
    db.add(nuevo_horario)
    db.commit()
    db.refresh(nuevo_horario)
    return nuevo_horario

@router.get("/", response_model=List[HorarioResponse])
def listar_horarioes(db: Session = Depends(get_db)):
    return db.query(Horario).all()

@router.get("/{id}", response_model=HorarioResponse)
def obtener_horario(id: int, db: Session = Depends(get_db)):
    horario = db.query(Horario).filter(Horario.id == id).first()
    if not horario:
        raise HTTPException(status_code=404, detail="Salón no encontrado")
    return horario

@router.put("/{id}", response_model=HorarioResponse)
def actualizar_horario(id: int, horario_actualizado: HorarioUpdate, db: Session = Depends(get_db)):
    horario = db.query(Horario).filter(Horario.id == id).first()
    if not horario:
        raise HTTPException(status_code=404, detail="Salón no encontrado")

    for key, value in horario_actualizado.model_dump().items():
        setattr(horario, key, value)

    db.commit()
    db.refresh(horario)
    return horario

@router.delete("/{id}")
def eliminar_horario(id: int, db: Session = Depends(get_db)):
    horario = db.query(Horario).filter(Horario.id == id).first()
    if not horario:
        raise HTTPException(status_code=404, detail="Salón no encontrado")

    db.delete(horario)
    db.commit()
    return {"message": "Salón eliminado exitosamente"}