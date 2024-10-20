import os
from helpers import validar_query,validar_inteiro, validar_texto
from produtos import Produto
from datetime import datetime

def rastreando_produto() -> bool:
    
        produto = Produto()
        # variavel para armazenar a query para usar o validar query, se caso vier vazio 
        query_localizacao = produto.trazer_produtos()
        
        print(query_localizacao.to_string(index=False))

        if not validar_query(query_localizacao):
            return False
        
        gerar_planinha = validar_texto("Deseja gerar uma planilha? y/n \n")

        if(gerar_planinha != "y"):
              return False
        
        data_hoje = datetime.now().strftime('%d-%m-%y_%H-%M')
        arquivo_excel = os.path.join('planilhas',f'Localizações_{data_hoje}.xlsx')
        
        try:
              query_localizacao.to_excel(arquivo_excel, index=False, engine="openpyxl")
              print(f"Relatório de localização salvo em {arquivo_excel}")
        except:
              print("Erro ao salvar o arquivo")
              return False

        return True