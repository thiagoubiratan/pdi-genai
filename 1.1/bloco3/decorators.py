# um decorator é uma função que envolve outra função
def meu_decorator(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

# aplicando o decorator com @
@meu_decorator
def saudacao():
    print("Olá!")

saudacao()
# Antes da função
# Olá!
# Depois da função

# exemplo prático — medindo tempo de execução
import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} executou em {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tempo
def processar():
    time.sleep(1)  # simula processamento de 1 segundo
    print("Processamento concluído")

processar()