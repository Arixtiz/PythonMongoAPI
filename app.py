from fastapi import FastAPI
from routes.registro import registro
from docs import tags_metadata

app = FastAPI(
    title="Prueba fastAPI & Mongo",
    description="by: Juan José Aristizabal Sarrazola",
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.include_router(registro)
