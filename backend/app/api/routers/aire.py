from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.api.models.aire import AireAcondicionado
from app.api.schemas.aire import AireCreate, AireUpdate, AireResponse
from typing import List

router = APIRouter(prefix="/aires", tags=["Aires Acondicionados"])

@router.post("/", response_model=AireResponse)
def crear_aire(aire: AireCreate, db: Session = Depends(get_db)):
    nuevo_aire = AireAcondicionado(**aire.model_dump())
    db.add(nuevo_aire)
    db.commit()
    db.refresh(nuevo_aire)
    return nuevo_aire

@router.get("/", response_model=List[AireResponse])
def todos_los_aires(db: Session = Depends(get_db)):
    return db.query(AireAcondicionado).all()

@router.get("/{id}", response_model=AireResponse)
def obtener_aire(id: int, db: Session = Depends(get_db)):
    aire = db.query(AireAcondicionado).filter(AireAcondicionado.id == id).first()
    if not aire:
        raise HTTPException(status_code=404, detail="Aire no encontrado")
    return aire

@router.put("/{id}", response_model=AireResponse)
def actualizar_aire(id: int, aire_actualizado: AireUpdate, db: Session = Depends(get_db)):
    aire = db.query(AireAcondicionado).filter(AireAcondicionado.id == id).first()
    if not aire:
        raise HTTPException(status_code=404, detail="Aire no encontrado")

    for key, value in aire_actualizado.model_dump().items():
        setattr(aire, key, value)

    db.commit()
    db.refresh(aire)
    return aire

@router.delete("/{id}")
def eliminar_aire(id: int, db: Session = Depends(get_db)):
    aire = db.query(AireAcondicionado).filter(AireAcondicionado.id == id).first()
    if not aire:
        raise HTTPException(status_code=404, detail="Aire no encontrado")
    
    db.delete(aire)
    db.commit()
    return {"message": "Aire eliminado exitosamente"}