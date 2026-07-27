usuario = "thiago"
senha = "1234"
idade = 20

if usuario == "thiago" and senha == "1234":
    if idade >= 18:
        print("Acesso liberado")
    else:
        print("Acesso negado — menor de idade")
else:
    print("Usuário ou senha incorretos")