from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.api.models.edificio import Edificio
from app.api.schemas.edificio import EdificioCreate, EdificioUpdate, EdificioResponse
from typing import List

router = APIRouter(prefix="/edificios", tags=["Edificios"])

@router.post("/",response_model=EdificioResponse)
def crear_edificio(edificio: EdificioCreate, db: Session = Depends(get_db)):
    nuevo_edificio = Edificio(**edificio.model_dump())
    db.add(nuevo_edificio)
    db.commit()
    db.refresh(nuevo_edificio)
    return nuevo_edificio

@router.get("/",response_model=List[EdificioResponse])
def todos_los_edificios(db: Session = Depends(get_db)):
    return db.query(Edificio).all()

@router.get("/{id}",response_model=EdificioResponse)
def obtener_edificio(id: int, db: Session = Depends(get_db)):
    edificio = db.query(Edificio).filter(Edificio.id == id).first()
    if not edificio:
        return HTTPException(status_code=404, detail="Edificio no encontrado")
    return edificio

@router.put("/{id}", response_model=EdificioResponse)
def modificar_edificio(id: int, edificio_actualizado: EdificioUpdate, db: Session = Depends(get_db)):
    edificio = db.query(Edificio).filter(Edificio.id == id).first()
    if not edificio:
        return HTTPException(status_code=404, detail="Edificio no encontrado")
    for key, value in edificio_actualizado.model_dump().items():
        setattr(edificio, key, value)
    db.commit()
    db.refresh(edificio)
    return edificio

@router.delete("/{id}")
def eliminar_edificio(id: int, db:Session = Depends(get_db)):
    edificio = db.query(Edificio).filter(Edificio.id == id).first()
    if not edificio:
        return HTTPException(status_code=404, detail="Edificio no encontrado")
    
    db.delete(edificio)
    db.commit()
    return { "mensaje": "Salón eliminado correctamente "}