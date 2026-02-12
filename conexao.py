import sqlite3
from pathlib import Path

ROOT_PATH = Path().parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(50) )"
    )
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()

#atualizar_registro(conexao, cursor, 'Adilson', 'adilson@gmail.com',1)

def delete_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes  WHERE id=?;', data)
    conexao.commit()


def inserir_many_registro(conexao, cursor,dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?);', dados)
    conexao.commit()

# criar_tabela(conexao,cursor)
# inserir_registro(conexao, cursor, 'Ana', 'email')
# inserir_registro(conexao, cursor, 'Adão', 'email')
# inserir_registro(conexao, cursor, 'Miguel', 'email')
# delete_registro(conexao, cursor, 2)

dados = (['João', 'barros@gmail.com'],['Edson', 'ed@gmail.com'],['Das menoras', 'menoras@gmail.com'])
inserir_many_registro(conexao, cursor,dados)