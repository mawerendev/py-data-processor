import sys
from src.data_processor import DataProcessor


def main():
    processor = DataProcessor()

    print("=== Procesador e Ingestor de Datos Locales ===")
    entrada = input("Ingresa un párrafo o texto largo para procesar: ")

    if not entrada.strip():
        print("Entrada vacía. Abortando.")
        sys.exit(1)

    print("\n[Procesando estructuras en disco...]")
    resultado = processor.analizar_y_guardar(entrada)

    print(f"\n{resultado}\n")


if __name__ == "__main__":
    main()