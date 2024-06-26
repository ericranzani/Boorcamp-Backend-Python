import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connect = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = connect.cursor()
cursor.row_factory = sqlite3.Row


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


# inserir varios registros
def inserir_muitos(connect, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    connect.commit()


# recuperar cliente
def recuperar_cliente(cursos, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_cliente(cursor, 1)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])
print(f'Seja bem vindo ao sistema {cliente["nome"]}')


# atualizar_registro(connect, cursor, "angelica", "angelica@gmail.com", id)
# inserir_registro(connect, cursor, "outro", "outro@gmail.com")
# excluir_registro(connect, cursor, 2)
# dados = [
#     ("teste1", "teste1@gmail.com"),
#     ("teste2", "teste2@gmail.com"),
#     ("teste3", "teste3@gmail.com"),
# ]
# inserir_muitos(connect, cursor, dados)
