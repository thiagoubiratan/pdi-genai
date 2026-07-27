# jeito tradicional com loop
numeros = []
for i in range(10):
    numeros.append(i)
print(numeros)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# com list comprehension — mesma coisa em uma linha
numeros = [i for i in range(10)]
print(numeros)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# com condição — só os pares
pares = [i for i in range(10) if i % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# transformando os valores — dobrando cada número
dobrados = [i * 2 for i in range(10)]
print(dobrados)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]