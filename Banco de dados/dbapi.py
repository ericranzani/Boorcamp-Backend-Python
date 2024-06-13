import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connect = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = connect.cursor()

cursor.execute(
    "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
)
