import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect("produtos.db")
cursor = conn.cursor()

# Inserindo alguns produtos
insert_produtos = """
INSERT INTO Produtos (nome, categoria, quantidade, preco, localizacao) 
VALUES 
    ('Caneta Azul', 'Escritório', 100, 1.50, 'Estoque A1'),
    ('Lápis', 'Escritório', 150, 0.75, 'Estoque A2'),
    ('Caderno', 'Escritório', 50, 15.00, 'Estoque B1'),
    ('Borracha', 'Escritório', 200, 0.50, 'Estoque A3'),
    ('Tesoura', 'Escritório', 75, 5.00, 'Estoque B2'),
    ('Calculadora', 'Eletrônicos', 20, 30.00, 'Estoque C1'),
    ('Notebook', 'Eletrônicos', 10, 2500.00, 'Estoque C2'),
    ('Teclado', 'Eletrônicos', 35, 120.00, 'Estoque C3'),
    ('Mouse', 'Eletrônicos', 50, 60.00, 'Estoque C4'),
    ('Fone de Ouvido', 'Eletrônicos', 80, 80.00, 'Estoque C5')
"""

cursor.execute(insert_produtos)

# Confirmando as mudanças
conn.commit()

# Fechando a conexão
conn.close()

print("Dados inseridos com sucesso!")
