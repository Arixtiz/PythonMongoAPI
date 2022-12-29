def registroEntity(item) -> dict:
    return{
        "id": str(item['_id']),
        "usuario_id": item['usuario_id'],
        "ano": item['ano'],
        "mes": item['mes'],
        "dia": item['dia'],
        "hora_entrada_definido": item['hora_entrada_definido'],
        "hora_salida_definido": item['hora_salida_definido'],
        "hora_entrada_real": item['hora_entrada_real'],
        "hora_salida_real": item['hora_salida_real'],
        "punto_de_entrada": item['punto_de_entrada'],
        "punto_de_salida": item['punto_de_salida'],
        "tipo_de_jornada": item['tipo_de_jornada'],
        "total_de_horas": item['total_de_horas'],
        "observaciones": item['observaciones'],
    }

def registrosEntity(entity) -> list:
    return[registroEntity(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i: str(a[i]) for i in a if i == '_id'}, **{i: a[i] for i in a if i != '_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]
