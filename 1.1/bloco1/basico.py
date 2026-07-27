# importações
import os

# variáveis globais / configurações
NOME_APP = "Meu App"

# funções
def saudacao(nome):
    return f"Olá, {nome}!"

# ponto de entrada
if __name__ == "__main__":
    resultado = saudacao("Thiago")
    print(resultado)