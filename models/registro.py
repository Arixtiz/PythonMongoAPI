from typing import Optional
from pydantic import BaseModel

class Registro(BaseModel):
    id: Optional[str]
    usuario_id:str
    ano:int
    mes:int
    dia:int
    hora_entrada_definido:int
    hora_salida_definido:int
    hora_entrada_real:int
    hora_salida_real:int
    punto_de_entrada:str
    punto_de_salida:str
    tipo_de_jornada:str
    total_de_horas:int
    observaciones:str