linhasMatriz = []
soma = 0

tamanhoMatriz = tuple(map(int, input().split()))

for i in range(tamanhoMatriz[0]):
    linhasMatriz.append(list(map(int, input().split())))

procurado = int(input())

for i in linhasMatriz:
    for c in i:
        if c == procurado:
            soma += 1

print(f'Ash pegou {soma} pokemon')