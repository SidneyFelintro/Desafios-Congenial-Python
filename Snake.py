linhasMatriz = []

tamanhoMatriz = tuple(map(int, input().split()))

for i in range(tamanhoMatriz[0]):
    linhasMatriz.append(list(map(int, input().split())))
def somandoMatriz():
    soma = 0
    for valor in linhasMatriz:
        for c in valor:
            soma += c
    return soma
print(somandoMatriz())