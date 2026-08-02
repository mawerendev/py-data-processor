import sys


def analizar_texto(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres = len(texto)

    print("\n--- RESULTADOS DEL ANÁLISIS ---")
    print(f"Total de caracteres: {num_caracteres}")
    print(f"Total de palabras: {num_palabras}")
    print("-------------------------------\n")


def main():
    print("=== Mi Primer Script en Python ===")
    entrada = input("Escribe una frase o texto para analizar: ")

    if entrada.strip():
        analizar_texto(entrada)
    else:
        print("No ingresaste ningún texto.")


if __name__ == "__main__":
    main()