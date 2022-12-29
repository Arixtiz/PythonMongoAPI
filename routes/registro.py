from fastapi import APIRouter, Response
from config.db import conn
from schemas.registro import registroEntity, registrosEntity
from models.registro import Registro
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

registro = APIRouter()

@registro.get('/registros', response_model=list[Registro], tags=["Registros"])
async def find_all_register():
    return registrosEntity(conn.local.registro.find())

@registro.post('/registro', response_model=Registro, tags=["Registros"])
async def create_register(reg: Registro):
    new_registro = dict(reg)
    del new_registro["id"]
    id = conn.local.registro.insert_one(new_registro).inserted_id
    return "Registro creado exitosamente!"

@registro.get('/registros/{id}',response_model=Registro, tags=["Registros"])
async def find_register(id: str):
    return registroEntity(conn.local.registro.find_one({"_id": ObjectId(id)}))

@registro.put('/registros/{id}',response_model=Registro, tags=["Registros"])
async def update_register(id: str, reg: Registro):
    conn.local.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(reg)})
    return registroEntity(conn.local.registro.find_one({"_id": ObjectId(id)}))

@registro.put('/registros/hora_entrada_definido/{id}', tags=["Editar horas"])
async def update_register_hora_entrada_definido(id: str, hora: int):
    conn.local.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"hora_entrada_definido":hora}})
    return registroEntity(conn.local.registro.find_one({"_id": ObjectId(id)}))

@registro.put('/registros/hora_salida_definido/{id}', tags=["Editar horas"])
async def update_register_hora_salida_definido(id: str, hora: int):
    conn.local.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"hora_salida_definido":hora}})
    return registroEntity(conn.local.registro.find_one({"_id": ObjectId(id)}))

@registro.put('/registros/hora_entrada_real/{id}', tags=["Editar horas"])
async def update_register_hora_entrada_real(id: str, hora: int):
    conn.local.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"hora_entrada_real":hora}})
    return registroEntity(conn.local.registro.find_one({"_id": ObjectId(id)}))

@registro.put('/registros/"hora_salida_real/{id}', tags=["Editar horas"])
async def update_register_hora_salida_real(id: str, hora: int):
    conn.local.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"hora_salida_real":hora}})
    return registroEntity(conn.local.registro.find_one({"_id": ObjectId(id)}))

@registro.put('/registros/"total_de_horas/{id}', tags=["Editar horas"])
async def update_register_total_de_horas(id: str, hora: int):
    conn.local.registro.find_one_and_update({"_id": ObjectId(id)}, {"$set": {"total_de_horas":hora}})
    return registroEntity(conn.local.registro.find_one({"_id": ObjectId(id)}))
    
    

@registro.delete('/registros/{id}', tags=["Registros"])
async def delete_register(id: str):
    registroEntity(conn.local.registro.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
