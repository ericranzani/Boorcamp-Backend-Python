import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connect = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = connect.cursor()


# criando a tabel e seus campos
def criar_tabela(cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    connect.commit()


# inserindo os dados em cada campo da tabela
def inserir_registro(connect, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    connect.commit()


# atualizando os dados em cada campo da tabela
def atualizar_registro(connect, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET NOME=?, EMAIL=? WHERE id=?;", data)
    connect.commit()


# deletando os dados em cada campo da tabela
def excluir_registro(connect, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    connect.commit()


# atualizar_registro(connect, cursor, "angelica", "angelica@gmail.com", id)
# inserir_registro(connect, cursor, "outro", "outro@gmail.com")
excluir_registro(connect, cursor, 2)
