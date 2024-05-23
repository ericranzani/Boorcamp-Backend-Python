from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc:
    # FileNotFoundError ativa quando arquivo que esta sendo aberto não é encontrado
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    # quando ocorre um erro geral
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")

# para linux
# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")