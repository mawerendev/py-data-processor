import json
import os
from typing import Dict, Any


class DataProcessor:
    """
    Handles data processing operations, including text metrics extraction
    and structured JSON report generation.
    """

    def __init__(self, output_folder: str = "reports"):
        self.output_folder = output_folder
        # Ensure output directory exists before processing
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    @staticmethod
    def process_text(text: str) -> Dict[str, Any]:
        """
        Extracts core structural metrics from the input string.
        Matches the interface expected by main.py and unit tests.
        """
        words = text.split()
        return {
            "char_count": len(text),
            "word_count": len(words),
            "longest_word": max(words, key=len) if words else "",
        }

    def analizar_y_guardar(self, text: str, filename: str = "reporte.json") -> str:
        """
        Analyzes the input text to extract structural metrics and saves
        the resulting dictionary into a formatted JSON file.
        """
        words = text.split()

        # Build structured data payload
        metrics: Dict[str, Any] = {
            "total_characters": len(text),
            "total_words": len(words),
            "longest_word": max(words, key=len) if words else "",
            "word_frequency": {
                w.lower(): words.count(w) for w in set(words)
            },
        }

        file_path = os.path.join(self.output_folder, filename)

        # Safe file writing operations
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(metrics, file, indent=4, ensure_ascii=False)
            return f"Report successfully generated at: {file_path}"
        except Exception as error:
            return f"Failed to write report to disk: {error}"