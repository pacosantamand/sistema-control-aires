from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from typing import Dict
from app.database import get_db
from app.api.models.aire import AireAcondicionado
from app.api.models.horario import Horario

router = APIRouter()

device_connections: Dict[int, WebSocket] = {}  
manual_control: Dict[int, bool] = {}  

async def verificar_estado_aire(aire_id: int, db: Session):
    aire = db.query(AireAcondicionado).filter(AireAcondicionado.id == aire_id).first()
    if not aire:
        return "Aire no encontrado"

    horario_actual = db.query(Horario).filter(
        Horario.aire_id == aire_id
    ).first()

    if horario_actual:
        return "Encender Aire" if horario_actual.aire_encendido else "Apagar Aire"

    return "Apagar Aire" 

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):

    await websocket.accept()
    aire_id = await websocket.receive_text()  # Recibe el ID del aire acondicionado desde Arduino
    print("aire id: ",aire_id)
    try:
        aire_id = int(aire_id)
        device_connections[aire_id] = websocket
        print(f"Conexión establecida con Aire ID {aire_id}")

        while True:
            estado = await verificar_estado_aire(aire_id, db)
            await websocket.send_text(estado)  # Enviar el estado del aire acondicionado
            print(f"Enviado a Aire {aire_id}: {estado}")

    except WebSocketDisconnect:
        print(f"Desconectado Aire ID {aire_id}")
        device_connections.pop(aire_id, None)

@router.post("/control_manual/{aire_id}")
async def control_manual(aire_id: int, encender: bool, db: Session = Depends(get_db)):
    aire = db.query(AireAcondicionado).filter(AireAcondicionado.id == aire_id).first()
    if not aire:
        return {"error": "Aire no encontrado"}

    aire.estado = encender
    db.commit()

    # Notificar al Arduino si está conectado
    if aire_id in device_connections:
        await device_connections[aire_id].send_text("Encender Aire" if encender else "Apagar Aire")
        print(f"Comando manual enviado a Aire {aire_id}: {'Encender' if encender else 'Apagar'}")

    return {"mensaje": "Estado actualizado manualmente"}