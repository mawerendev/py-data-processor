import sys
from src.ai_engine import AIEngine


def main():
    # Creamos una instancia de nuestro motor de IA
    motor = AIEngine(model_name="llama3.2")

    print("=== Servidor Local de IA (Estructura Modular) ===")
    entrada = input("Ingresa tu pregunta: ")

    if not entrada.strip():
        print("No ingresaste ningún texto.")
        return

    print("\n[Procesando con el motor local...]")
    respuesta = motor.consultar(entrada)

    print("\n--- RESPUESTA ---")
    print(respuesta)
    print("-----------------\n")


if __name__ == "__main__":
    main()