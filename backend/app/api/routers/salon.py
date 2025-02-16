from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.api.models.salon import Salon
from app.api.schemas.salon import SalonCreate, SalonUpdate, SalonResponse
from typing import List

router = APIRouter(prefix="/salones", tags=["Salones"])

@router.post("/",response_model=SalonResponse)
def crear_salon(salon: SalonCreate, db: Session = Depends(get_db)):
    nuevo_salon = Salon(**salon.model_dump())
    db.add(nuevo_salon)
    db.commit()
    db.refresh(nuevo_salon)
    return nuevo_salon

@router.get("/",response_model=List[SalonResponse])
def todos_los_salones(db: Session = Depends(get_db)):
    return db.query(Salon).all()

@router.get("/{id}",response_model=SalonResponse)
def obtener_salon(id: int, db: Session = Depends(get_db)):
    salon = db.query(Salon).filter(Salon.id == id).first()
    if not salon:
        return HTTPException(status_code=404, detail="Salon no encontrado")
    return salon

@router.put("/{id}", response_model=SalonResponse)
def modificar_salon(id: int, salon_actualizado: SalonUpdate, db: Session = Depends(get_db)):
    salon = db.query(Salon).filter(Salon.id == id).first()
    if not salon:
        return HTTPException(status_code=404, detail="Salon no encontrado")
    for key, value in salon_actualizado.model_dump().items():
        setattr(salon, key, value)
    db.commit()
    db.refresh(salon)
    return salon

@router.delete("/{id}")
def eliminar_salon(id: int, db:Session = Depends(get_db)):
    salon = db.query(Salon).filter(Salon.id == id).first()
    if not salon:
        return HTTPException(status_code=404, detail="Salon no encontrado")
    
    db.delete(salon)
    db.commit()
    return { "mensaje": "Salón eliminado correctamente "}