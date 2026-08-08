import pytest
from fastapi.testclient import TestClient
from main import app

# Instanciar el cliente de prueba conectado a la aplicación de FastAPI
client = TestClient(app)


def test_health_check_endpoint():
    """Verifica que el endpoint raíz responda 200 OK y el estado activo."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "online",
        "message": "API de Procesamiento de Datos activa"
    }


def test_process_text_success():
    payload = {
        "content": "Pytest y FastAPI garantizan la calidad del software"
    }
    response = client.post("/api/v1/process-text", json=payload)
    
    # Si falla, esto nos imprimirá la causa exacta en la consola de pytest
    print("DETALLE DEL ERROR:", response.json())
    
    assert response.status_code == 201


def test_process_text_empty_content_validation():
    """Verifica que Pydantic / FastAPI rechacen un texto de solo espacios en blanco."""
    payload = {
        "content": "   "
    }
    response = client.post("/api/v1/process-text", json=payload)
    
    # Debe retornar un error 400 Bad Request
    assert response.status_code == 400
    assert "detail" in response.json()