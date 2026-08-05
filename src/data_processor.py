import json
import os
from typing import Dict, Any


class DataProcessor:

    def __init__(self, output_folder: str = "reports"):
        self.output_folder = output_folder
        # Crea la carpeta de reportes si no existe
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def analizar_y_guardar(self, texto: str, filename: str = "reporte.json") -> str:
        """Analiza la estructura del texto y exporta las métricas a un JSON."""
        palabras = texto.split()

        # Construcción de estructura de datos
        metricas: Dict[str, Any] = {
            "total_caracteres": len(texto),
            "total_palabras": len(palabras),
            "palabra_mas_larga": (
                max(palabras, key=len) if palabras else ""
            ),
            "frecuencia_palabras": {
                p.lower(): palabras.count(p) for p in set(palabras)
            },
        }

        file_path = os.path.join(self.output_folder, filename)

        # Escritura segura de archivo en disco
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(metricas, f, indent=4, ensure_ascii=False)
            return f"Reporte guardado exitosamente en: {file_path}"
        except Exception as e:
            return f"Error al escribir en disco: {e}"