# escrevendo em um arquivo
with open("teste.txt", "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

# lendo o arquivo inteiro
with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# lendo linha por linha
with open("teste.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove o \n do final

# adicionando conteúdo sem apagar o que já existe
with open("teste.txt", "a") as arquivo:
    arquivo.write("Terceira linha\n")