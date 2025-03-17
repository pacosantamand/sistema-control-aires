from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.api.models.aire import AireAcondicionado
from app.api.models.horario import Horario
from datetime import datetime
import asyncio

router = APIRouter()

device_connections = {}  # Diccionario para conexiones activas
control_manual = {}  # Diccionario para almacenar si un aire fue modificado manualmente

async def verificar_estado_aire(aire_id: int, db: Session):
    aire = db.query(AireAcondicionado).filter(AireAcondicionado.id == aire_id).first()
    if not aire:
        return "Aire no encontrado"

    dias_actual = {
        "Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles",
        "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado",
        "Sunday": "Domingo"
    }
    dia_actual = dias_actual[datetime.today().strftime("%A")]
    hora_actual = datetime.now().time()

    # Buscar horario activo
    horario = db.query(Horario).filter(
        Horario.aire_id == aire_id,
        Horario.dia == dia_actual,
        Horario.hora_inicio <= hora_actual,
        Horario.hora_fin >= hora_actual
    ).first()

    if aire_id in control_manual:
        return "Mantener Manual: Encendido" if control_manual[aire_id] else "Mantener Manual: Apagado"

    # Si hay un horario activo, encender automáticamente
    if horario:
        nuevo_estado = True
    else:
        nuevo_estado = False
        control_manual.pop(aire_id, None)  # Si termina el horario, eliminar restricción manual

    # Solo actualizar si hay un cambio real de estado
    if aire.estado != nuevo_estado:
        aire.estado = nuevo_estado
        db.commit()

    return "Encender Aire" if nuevo_estado else "Apagar Aire"

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    
    try:
        aire_id = await websocket.receive_text()
        aire_id = int(aire_id)

        if aire_id not in device_connections:
            device_connections[aire_id] = []
        device_connections[aire_id].append(websocket)

        print(f"Conexión establecida con Aire ID {aire_id}")

        while True:
            with next(get_db()) as session:
                estado = await verificar_estado_aire(aire_id, session)
            
            for ws in device_connections[aire_id]:
                try:
                    await ws.send_text(estado)
                except Exception:
                    pass  
            
            print(f"Enviado a Aire {aire_id}: {estado}")
            await asyncio.sleep(10)

    except WebSocketDisconnect:
        print(f"Desconectado Aire ID {aire_id}")
        if aire_id in device_connections:
            device_connections[aire_id].remove(websocket)
            if not device_connections[aire_id]:
                del device_connections[aire_id]

@router.post("/control_manual/{aire_id}")
async def control_manual_handler(aire_id: int, encender: bool, db: Session = Depends(get_db)):
    aire = db.query(AireAcondicionado).filter(AireAcondicionado.id == aire_id).first()
    if not aire:
        return {"error": "Aire no encontrado"}

    aire.estado = encender
    db.commit()
    
    control_manual[aire_id] = encender

    if aire_id in device_connections:
        for ws in device_connections[aire_id]:
            try:
                await ws.send_text("Encender Aire" if encender else "Apagar Aire")
            except Exception:
                pass  

    print(f"Comando manual enviado a Aire {aire_id}: {'Encender' if encender else 'Apagar'}")
    return {"mensaje": "Estado actualizado manualmente"}