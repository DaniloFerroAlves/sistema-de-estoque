import pandas as pd
import os

# limpar console
def limpar_console():
    #se for windows usa 'cls' se não clear
    os.system('cls' if os.name == 'nt' else 'clear')

#validar resultado de query
def validar_query(query: pd.DataFrame) -> bool:
    if query.empty:
        print("Não há esses dados no banco de dados!!")
        return False
    else:
        return True


# enquanto for verdade essas funções não saem do loop
def validar_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor.strip() == "":
            print("O valor não pode ser vazio!!!")
        else:
            return valor

def validar_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("O valor não pode ser negativo!!!")
            else:
                return valor
        except ValueError:
            print("Por favor, insira um número inteiro válido!!!")

def validar_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo!!!")
            else:
                return valor
        except ValueError:
            print("Por favor, insira um número válido!!!")