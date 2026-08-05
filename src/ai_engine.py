import ollama


class AIEngine:

    def __init__(self, model_name: str = "llama3.2"):
        self.model_name = model_name

    def consultar(self, prompt: str) -> str:
        """Envía la consulta al servidor local de Ollama."""
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un asistente técnico conciso y directo.",
                    },
                    {"role": "user", "content": prompt},
                ],
            )
            return response["message"]["content"]
        except Exception as e:
            return f"Error al conectar con el motor local: {e}"