qtdPessoas = int(input())
idsPessoas = list(map(int, input().split()))
desistentes = int(input())
idsDesistentes = list(map(int, input().split()))

resultado = [x for x in idsPessoas if x not in idsDesistentes]

for i in resultado:
    print(i, end=" ")