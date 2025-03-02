from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.api.models.bitacora import Bitacora
from app.api.schemas.bitacora import BitacoraCreate,  BitacoraResponse
from typing import List
from datetime import date

router = APIRouter(prefix="/bitacora", tags=["bitacora"])

@router.post("/",response_model=BitacoraResponse)
def crear_bitacora(bitacora: BitacoraCreate, db: Session = Depends(get_db)):
    nuevo_bitacora = Bitacora(**bitacora.model_dump())
    db.add(nuevo_bitacora)
    db.commit()
    db.refresh(nuevo_bitacora)
    return nuevo_bitacora

@router.get("/",response_model=List[BitacoraResponse])
def todos_los_bitacoras(db: Session = Depends(get_db)):
     return db.query(Bitacora).all()
    
@router.get("/{id}", response_model=BitacoraResponse)
def obtener_bitacora(id: int, db: Session = Depends(get_db)):
    bitacora = db.query(Bitacora).filter(Bitacora.id == id).first()
    if not bitacora:
        raise HTTPException(status_code=404, detail="Bitacora no encontrada")
    return bitacora

@router.get("/dia/{fecha}", response_model = List[BitacoraResponse])
def bitacora_por_dia(fecha: str, db: Session = Depends(get_db)):
    bitacora = db.query(Bitacora).filter(func.date(Bitacora.fecha) == fecha).all()
    return bitacora

@router.get("/desde/{fecha_inicio}/hasta/{fecha_fin}", response_model=List[BitacoraResponse])
def bitacora_por_rango(fecha_inicio: str, fecha_fin: str, db: Session = Depends(get_db)):
    bitacora = db.query(Bitacora).filter(func.date(Bitacora.fecha).between(fecha_inicio,fecha_fin)).all()
    return bitacora

@router.get("/dia", response_model = List[BitacoraResponse])
def bitacora_por_dia2(
    fecha: date = Query(..., description="Fecha de inicio (YYYY-MM-DD)"), db: Session = Depends(get_db)):   
    bitacora = db.query(Bitacora).filter(func.date(Bitacora.fecha) == fecha).all()
    return bitacora

@router.get("/rango",response_model=List[BitacoraResponse])
def bitacora_por_rango2(
    fecha_inicio: date = Query(..., description="Fecha de inicio (YYYY-MM-DD)"), 
    fecha_fin: date = Query(..., description="Fecha de inicio (YYYY-MM-DD)"), 
    db: Session = Depends(get_db)):
    bitacora = db.query(Bitacora).filter(func.date(Bitacora.fecha).between(fecha_inicio,fecha_fin)).all()
    return bitacora