# função normal
def dobrar(x):
    return x * 2

# mesma função como lambda
dobrar = lambda x: x * 2

print(dobrar(5))  # resultado: 10

# lambda com dois parâmetros
somar = lambda a, b: a + b
print(somar(3, 4))  # resultado: 7

# muito usado com sorted e filter
numeros = [5, 2, 8, 1, 9, 3]

# ordenar a lista
ordenados = sorted(numeros, key=lambda x: x)
print(ordenados)  # [1, 2, 3, 5, 8, 9]

# filtrar só os maiores que 4
maiores = list(filter(lambda x: x > 4, numeros))
print(maiores)  # [5, 8, 9]