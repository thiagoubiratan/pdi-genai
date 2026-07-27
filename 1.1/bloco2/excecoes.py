# sem tratamento — gera erro e para o programa
#numero = int("abc")  # ValueError: invalid literal

# com tratamento
try:
    numero = int("abc")
    print(numero)
except ValueError:
    print("Valor inválido — não é um número")

# capturando erros diferentes
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não permitida")
except ValueError:
    print("Valor inválido")

# finally — executa sempre, com ou sem erro
try:
    numero = int("123")
    print(f"Número: {numero}")
except ValueError:
    print("Valor inválido")
finally:
    print("Isso sempre executa")