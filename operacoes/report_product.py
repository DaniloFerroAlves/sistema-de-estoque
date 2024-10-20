import matplotlib.pyplot as plt
from helpers import validar_inteiro, limpar_console, validar_query
from produtos import Produto
from datetime import datetime
import os

def gerando_relatorio()-> bool:

        produto = Produto()
        print("Bem-vindo ao gerador de relatórios!")

        estoquebaixo_ou_movimentacao = validar_inteiro("1 - Gerar relatório de produtos com baixo estoque \n2 - Gerar relatório de movimentação de produtos \n") 

        limpar_console()

        if estoquebaixo_ou_movimentacao > 2 or estoquebaixo_ou_movimentacao < 0: # erro
                print("Por favor, selecione se é entrada ou saida corretamente, 1 ou 2")
        else:
                if estoquebaixo_ou_movimentacao == 1: # gerar estoque baixo
                        qtd_produtos = validar_inteiro("Informe a quantidade de produtos com o menor estoque que você deseja visualizar: \n")

                        limpar_console()

                        relatorio = produto.produtos_com_pouco_estoque(qtd_produtos)

                        # validar query - retorna false ele dá erro
                        if not validar_query(relatorio): # se retornar false
                                return False # retornar false

                        print(relatorio)

                        return True
                else: # gerar planilha excel movimentacao 
                      movimentacao = produto.movimentacao_de_produtos()  

                      if not validar_query(movimentacao):
                              print("Nenhuma movimentação encontrada")
                              return False
                                   
                      data_hoje = datetime.now().strftime('%d-%m-%y_%H-%M')
                      arquivo_excel = os.path.join('planilhas', f'Movimentação_{data_hoje}.xlsx')
     
                      try:
                              movimentacao.to_excel(arquivo_excel, index=False, engine='openpyxl')
                              print(f"Relatório de movimentação salvo em: {arquivo_excel}")
                      except:
                              print("Erro ao salvar o arquivo")
                              return False

                              


                

                              




