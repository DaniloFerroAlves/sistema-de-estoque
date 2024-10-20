import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def conectar_ao_db():
    return sqlite3.connect("produtos.db")

# constructor do produto com métodos

class Produto:
    def __init__(self, nome: str = None, categoria: str = None, quantidade: int = 0, preco: float = 0.0, localizacao: str = None):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao


    # Register movimentação
    def registrar_movimentacao(self, id, qtd, tipo):
        with conectar_ao_db() as conn:
            query = """
                INSERT INTO Movimentacao (produto_id, quantidade, tipo, data)
                VALUES (?, ?, ?, ?)
            """

            data_atual = datetime.now().strftime('%d/%m/%Y, %H:%M')

            cursor = conn.cursor()

            if tipo == 1: #entrada
                cursor.execute(query, (id, qtd, 'entrada', data_atual))
                conn.commit()
                print(f'Movimentação registrada: Entrada de {qtd} unidades do produto')
            else: # saida
                cursor.execute(query, (id, qtd, 'saida', data_atual))
                conn.commit()
                print(f'Movimentação registrada: Saída de {qtd} unidades do produto')

    # Selecionar dados
    def trazer_produtos(self, id: int = None) -> pd.DataFrame:
        with conectar_ao_db() as conn:
            #seleciona se vier id
            if id is not None:
                query = """SELECT * 
                        FROM Produtos 
                        WHERE id = ?"""
                select_query = pd.read_sql_query(query, conn, params=(id,))
                return select_query
            else: # Seleciona se tudo se não vier id
                select_query = pd.read_sql_query("SELECT * FROM Produtos", conn)
                return select_query
    
    # Trazer localização
    # def trazer_todas_localizacao(self, produto: str = None) -> pd.DataFrame:
    #     with conectar_ao_db() as conn:
    #         # trazer localizacao escolhida
    #         if produto is not None:
    #             query = """SELECT * 
    #                     FROM Produtos 
    #                     WHERE produto 
    #                     LIKE ?"""
    #             select_query = pd.read_sql_query(query, conn, params=(f'%{produto}%',))
    #             return select_query

    #         else: # trazer todas localizaçoes para escolher
    #             query = """SELECT localizacao, SUM(quantidade) AS total_produtos 
    #                         FROM produtos WHERE quantidade > 0 
    #                         GROUP BY localizacao"""
    #             select_query = pd.read_sql_query(query, conn)
    #             return select_query


    # Trazer categorias
    def trazer_todas_categorias(self) -> pd.DataFrame:
        with conectar_ao_db() as conn:
            query = """SELECT DISTINCT categoria as 'Categorias Disponiveis' 
                    FROM Produtos"""

            select_query = pd.read_sql_query(query, conn)

            return select_query
  
    # Adicionar produto
    def adicionar_produto(self) -> None:
        with conectar_ao_db() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Produtos (nome, categoria, quantidade, preco, localizacao) 
                VALUES (?, ?, ?, ?, ?)
            """, (self.nome, self.categoria, self.quantidade, self.preco, self.localizacao))

            conn.commit()
            print("Produto adicionado com sucesso")
            self.trazer_produtos()

    # Atualizar estoque do produto
    def atualizar_estoque(self, id: int, qtd: int, tipo = 1) -> None:

        with conectar_ao_db() as conn:
            cursor = conn.cursor()

            # pegar quantidade atual
            cursor.execute("""
                SELECT nome, quantidade 
                FROM produtos 
                WHERE id = ?
            """, (id,))

            # trazer 1 linha
            resultado = cursor.fetchone()

            # tipo 1 - entrada 
            # tipo 2 - saida
            if tipo == 1:
                if resultado:
                    # desestruturando a tupla que vem do sql
                    nome, quantidade_atual = resultado 

                    # soma da quantidade que esta no bd e com a quantidade escolhida
                    quantidade_atualizada = int(qtd) + int(quantidade_atual)

                    cursor.execute("""
                    UPDATE Produtos 
                    SET quantidade = ? 
                    WHERE id = ?
                    """, (quantidade_atualizada, id,))

                    conn.commit()

                    print(f"O Estoque do produto {nome} aumentou para {quantidade_atualizada}")
                    self.trazer_produtos(id)
                else:
                    print("Produto não encontrado")
            elif tipo == 2:
                    if resultado:
                        # desestruturando a tupla que vem do sql
                        nome, quantidade_atual = resultado 
                        # soma da quantidade que esta no bd e com a quantidade escolhida
                        if quantidade_atual < qtd:
                            print("Você não pode escolher uma quantidade maior do que a quantidade de estoque atual!!")
                        else:
                            quantidade_atualizada = int(quantidade_atual) - int(qtd) 

                            cursor.execute("""
                            UPDATE Produtos 
                            SET quantidade = ? 
                            WHERE id = ?
                            """, (quantidade_atualizada, id,))

                            conn.commit()

                            print(f"O Estoque do produto {nome} diminuiu para {quantidade_atualizada}")
                            self.trazer_produtos(id)
                    else:
                        print("Produto não encontrado")
            else:
                print("Escolha um número entre 1 - Entrada e 2 - Saída")

    
    #Gerar relatorio c grafico com produtos com baixo estoque, com base na quantidade de produtos
    def produtos_com_pouco_estoque(self, qtd) -> pd.DataFrame:
        with conectar_ao_db() as conn:
        
            query = """SELECT nome, quantidade 
                        FROM Produtos
                        ORDER BY quantidade 
                        ASC LIMIT ?"""
            select_query = pd.read_sql_query(query, conn, params=(qtd,))

            # gerar gráfico de barras com estoque dos 5 produtos com menor estoque
            plt.bar(select_query['nome'], select_query['quantidade'], color='orange')

            plt.xlabel('Produtos') # Horz
            plt.ylabel('Quantidade de estoque') # Vert
            plt.title(f'Os {qtd} produtos com menor estoque') 
            plt.show()


            return select_query
        
    # Gerar relatorio de movimentação
    def movimentacao_de_produtos(self) -> pd.DataFrame:
        with conectar_ao_db() as conn:
            query = """SELECT Movimentacao.quantidade, Movimentacao.data, Movimentacao.tipo, Produtos.nome 
                        FROM Movimentacao
                        JOIN Produtos ON Movimentacao.produto_id = Produtos.id
                        """
            select_query = pd.read_sql_query(query, conn)
            return select_query

