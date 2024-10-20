# Criação db
import sqlite3

conn = sqlite3.connect("produtos.db")

cursor = conn.cursor()

create_table_movimentacao = """
CREATE TABLE IF NOT EXISTS Movimentacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES Produtos (id)
)
"""

create_table_produto = """
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL,
    localizacao TEXT NOT NULL
)
"""

cursor.execute(create_table_produto)
cursor.execute(create_table_movimentacao)

print("Tabelas criadas com sucesso!!")

conn.commit()
conn.close()
# Criação db end.