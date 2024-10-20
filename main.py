from helpers import validar_inteiro, validar_texto, validar_query, limpar_console
from produtos import Produto
# operacoes
from operacoes.add_product import adicionando_produto
from operacoes.update_product import atualizando_produto
from operacoes.track_product import rastreando_produto
from operacoes.report_product import gerando_relatorio

# Contador pra saber se já fez alguma operação
count = 0 

# instancia do meu produto
produto = Produto() 
# tarefas a serem executadas dependendo da resposta do usuario
while True:
    # se ja tiver feito alguam operação ele pergunta e dependendo da resposta ele sai ou continua no programa
    if count > 0: 
        resposta = input("Deseja fazer alguma outra operação? y/n \n").lower()
        if resposta == "y":
            count = 0
            limpar_console()
            continue
        else:
            break
    else:
        # arr de tipos de operações para a pessoa escolher
        operacoes = [
            "1 - Novo produto", 
            "2 - Atualizar estoque", 
            "3 - Rastrear produto", 
            "4 - Criar relatório", 
            "5 - Sair"]

        print("Bem-vindo ao sistema gerenciador de estoque, o que você deseja fazer?")

        for operacao in operacoes: print(operacao) # iterando sobre o arr de opções

        # pegando a resposta 
        resposta_operacao = validar_inteiro("Escolha qual você deseja com base no numeração: ")

        limpar_console()

    if resposta_operacao == 1: # Adicionar produto
        count += 1
        adicionando_produto()

    elif resposta_operacao == 2: # Atualizar estoque

        count += 1
        # Se retonar false quer dizer que não há dados vindo da query
        if not atualizando_produto(): # Só uma validação se caso a query venha sozinha
            continue

    elif resposta_operacao == 3: # Rastrear produto por localização
        count += 1
        # Se retonar false quer dizer que não há dados vindo da query
        if not rastreando_produto(): # Só vai invocar a função caso venha true do validar_query
            continue
    elif resposta_operacao == 4:
        count += 1
        if not gerando_relatorio():
            continue
    elif resposta_operacao == 5: # Sair do sistema
        print("Saindo do sistema...")
        break
    else:
        print("Operação inválida!")
















