from helpers import validar_inteiro, validar_texto, validar_float
from produtos import Produto


def adicionando_produto() -> None:

        produto = Produto()
        print("Você entrou para cadastrar um produto")
        
        nome = validar_texto("Digite o nome do produto: ")

        # mostrar todas as categorias para controlar melhor os tipos de produtos
        todas_categorias = produto.trazer_todas_categorias()
        print(todas_categorias.to_string(index=False))

        categoria = validar_texto("Digite a categoria do produto: ")
        quantidade = validar_inteiro("Digite a quantidade do produto: ")
        preco = validar_float("Digite o preço do produto: ")
        localizacao = validar_texto("Digite a localização do produto: ")

        print(f"Produto: {nome}, Categoria: {categoria}, Quantidade: {quantidade}, Preço: {preco}, Localização: {localizacao}")


        produto = Produto(nome, categoria, quantidade, preco, localizacao)
        produto.adicionar_produto()