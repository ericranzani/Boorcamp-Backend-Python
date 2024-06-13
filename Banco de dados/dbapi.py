import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connect = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = connect.cursor()

# criando a tabel e seus campos
# cursor.execute(
# "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
# )

# inserindo os dados em cada campo da tabela
data = ("bruno", "bruno.ranzani20@gmail.com")
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
connect.commit()
