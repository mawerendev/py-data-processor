import sys
from src.data_processor import DataProcessor
from src.db_manager import DatabaseManager


def main():
    processor = DataProcessor()
    db = DatabaseManager()

    print("=== Engine de Datos e Ingestión SQL ===")
    print("1. Procesar nuevo texto y guardar en BD")
    print("2. Ver historial de reportes en BD")
    opcion = input("Selecciona una opción (1 o 2): ").strip()

    if opcion == "1":
        entrada = input("\nIngresa el texto a analizar: ")
        if not entrada.strip():
            print("Entrada vacía. Operación cancelada.")
            return

        # Calculamos métricas y guardamos en SQLite
        words = entrada.split()
        longest = max(words, key=len) if words else ""
        
        record_id = db.save_report(
            text=entrada,
            total_chars=len(entrada),
            total_words=len(words),
            longest_word=longest
        )
        print(f"\n[Exito] Reporte insertado en la base de datos con ID: {record_id}\n")

    elif opcion == "2":
        registros = db.fetch_all_reports()
        print(f"\n--- HISTORIAL DE REGISTROS EN BD ({len(registros)}) ---")
        for r in registros:
            print(f"ID: {r['id']} | Palabras: {r['total_words']} | Creado: {r['created_at']}")
            print(f"   Texto: '{r['input_text'][:40]}...'")
            print(f"   Palabra más larga: '{r['longest_word']}'\n")
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()