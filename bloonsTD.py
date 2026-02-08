tempo = int(input())
macacos = int(input())
dano = tuple(map(int, input().split()))


def calculo():
    soma = 0
    for i, d in enumerate(dano):
        soma += dano[i]
    pontos = (soma * tempo)

    return pontos

if calculo() >= 28000:
    print('Macacos venceram!')
else:
    print('O BAD venceu!')