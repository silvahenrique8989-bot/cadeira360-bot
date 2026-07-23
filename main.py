"""
Cadeira360
Arquivo principal do projeto.

Responsável por iniciar a execução do monitor.
"""

from bot import executar


def main():
    print("=" * 50)
    print("Cadeira360 v2.0")
    print("=" * 50)

    try:
        executar()
    except KeyboardInterrupt:
        print("Execução interrompida pelo usuário.")
    except Exception as erro:
        print(f"Erro durante a execução: {erro}")


if __name__ == "__main__":
    main()
