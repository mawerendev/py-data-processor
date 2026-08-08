from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import uvicorn

from src.db_manager import DatabaseManager
from src.data_processor import DataProcessor

# Inicializar la aplicación FastAPI
app = FastAPI(
    title="Data Processor & Analytics API",
    description="API REST para procesar métricas de texto y persistirlas en SQLite.",
    version="1.0.0"
)

# Instanciar servicios (DatabaseManager ya crea la tabla al inicializarse en su __init__)
db_manager = DatabaseManager()

# Esquema de Pydantic para validar la petición HTTP entrante
class TextProcessRequest(BaseModel):
    content: str = Field(
        ...,
        min_length=1,
        description="El texto a procesar. No puede estar vacío.",
        examples=["Hola mundo desde FastAPI"]
    )


# Esquema de Pydantic para estructurar la respuesta HTTP exitosa
class TextProcessResponse(BaseModel):
    id: int
    content: str
    char_count: int
    word_count: int
    longest_word: str
    status: str = "success"


@app.get("/", tags=["Health Check"])
def read_root():
    """Endpoint de salud para verificar que el servidor está corriendo."""
    return {"status": "online", "message": "API de Procesamiento de Datos activa"}


@app.post(
    "/api/v1/process-text",
    response_model=TextProcessResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Metrics Processing"]
)
def process_and_save_text(request: TextProcessRequest):
    """
    Endpoint HTTP que:
    1. Recibe y valida el texto entrante vía Pydantic.
    2. Procesa las métricas (caracteres, palabras, palabra más larga).
    3. Persiste el resultado en SQLite.
    4. Devuelve la respuesta estructurada en JSON.
    """
    raw_text = request.content.strip()

    if not raw_text:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El texto no puede contener únicamente espacios en blanco."
        )

    try:
        # 1. Calcular métricas
        metrics = DataProcessor.process_text(raw_text)

        # 2. Persistir en la base de datos
        record_id = db_manager.save_report(
            content=raw_text,
            char_count=metrics["char_count"],
            word_count=metrics["word_count"],
            longest_word=metrics["longest_word"]
        )

        # 3. Retornar la respuesta tipada
        return TextProcessResponse(
            id=record_id,
            content=raw_text,
            char_count=metrics["char_count"],
            word_count=metrics["word_count"],
            longest_word=metrics["longest_word"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al procesar y guardar la información: {str(e)}"
        )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)