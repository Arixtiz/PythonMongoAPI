from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from config.db import db
from schemas.registro import registroEntity, registrosEntity
from models.registro import Registro
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

registro = APIRouter()

def error():
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops!. There goes a rainbow..."},
    )

@registro.get('/registros', response_model=list[Registro], tags=["Registros"])
async def find_all_register():
    try:
        return registrosEntity(db.registro.find())
    except:
        return "No hay registros"

@registro.post('/registro', tags=["Registros"])
async def create_register(reg: Registro):
    try:
        new_registro = dict(reg)
        del new_registro["id"]
        id = db.registro.insert_one(new_registro).inserted_id
        return "Registro creado exitosamente!"
    except:
        error()

@registro.get('/registros/{id}', tags=["Registros"])
async def find_register(id: str):
    try:
        return registroEntity(db.registro.find_one({"_id": ObjectId(id)}))
    except:
        error()

@registro.put('/registros/{id}', tags=["Registros"])
async def update_register(id: str, reg: Registro):
    try:
        db.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(reg)})
        return registroEntity(db.registro.find_one({"_id": ObjectId(id)}))
    except:
        error()

@registro.put('/registros/hora_entrada_definido/{id}', tags=["Editar horas"])
async def update_register_hora_entrada_definido(id: str, hora: int):
    try:
        db.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"hora_entrada_definido":hora}})
        return registroEntity(db.registro.find_one({"_id": ObjectId(id)}))
    except:
        error()

@registro.put('/registros/hora_salida_definido/{id}', tags=["Editar horas"])
async def update_register_hora_salida_definido(id: str, hora: int):
    try:
        db.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"hora_salida_definido":hora}})
        return registroEntity(db.registro.find_one({"_id": ObjectId(id)}))
    except:
        error()

@registro.put('/registros/hora_entrada_real/{id}', tags=["Editar horas"])
async def update_register_hora_entrada_real(id: str, hora: int):
    try:
        db.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"hora_entrada_real":hora}})
        return registroEntity(db.registro.find_one({"_id": ObjectId(id)}))
    except:
        error()

@registro.put('/registros/"hora_salida_real/{id}', tags=["Editar horas"])
async def update_register_hora_salida_real(id: str, hora: int):
    try:
        db.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"hora_salida_real":hora}})
        return registroEntity(db.registro.find_one({"_id": ObjectId(id)}))
    except:
        error()

@registro.put('/registros/"total_de_horas/{id}', tags=["Editar horas"])
async def update_register_total_de_horas(id: str, hora: int):
    try:
        db.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"total_de_horas":hora}})
        return registroEntity(db.registro.find_one({"_id": ObjectId(id)}))
    except:
        error()
    
@registro.delete('/registros/{id}', tags=["Registros"])
async def delete_register(id: str):
    try:
        registroEntity(db.registro.find_one_and_delete({"_id": ObjectId(id)}))
        return Response(status_code=HTTP_204_NO_CONTENT)
    except:
        error()
