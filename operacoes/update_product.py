from helpers import validar_inteiro, validar_texto, validar_float, validar_query, limpar_console
from produtos import Produto

def atualizando_produto() -> bool:
        
        produto = Produto()

        print("Voce entrou para atualizar o estoque")

        # armazenando a query em uma variavel para poder validar
        query_produto = produto.trazer_produtos()

        print(query_produto.to_string(index=False))

        if not validar_query(query_produto): 
            return False
        


        # pegar qual produto vai ser atualizado
        id_produto = validar_inteiro("Escolha qual você deseja atualizar com base no ID\n")
        limpar_console()

        print("Você escolheu o produto:")
        # Trazer produto com base no numero que escolher
        produto_trazido = produto.trazer_produtos(id_produto)
        print(produto_trazido.to_string(index=False))

        while True:
        # aumento ou diminuição de estoque
            tipo_entrada_ou_saida = validar_inteiro("1 - Entrada de estoque \n2 - Saida de estoque \n") 

            if tipo_entrada_ou_saida > 2 or tipo_entrada_ou_saida < 0:
                 print("Por favor, selecione se é entrada ou saida corretamente, 1 ou 2")
            else:
                # Pegar a quantidade que vai estocada
                qtd_produto = validar_inteiro("Qual vai ser a quantidade?\n")

                limpar_console()
                # registrar atualização de estoque
                produto.registrar_movimentacao(id_produto, qtd_produto, tipo_entrada_ou_saida) 
                produto.atualizar_estoque(id_produto ,qtd_produto, tipo_entrada_ou_saida)
                return True

