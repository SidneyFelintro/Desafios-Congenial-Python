def range_capacidade():
    capacidade = int(input())
    return list(range(1, capacidade + 1))


def assentos():
    qtd_assentos_ocupados = int(input())
    if qtd_assentos_ocupados != 0 :
        assentos_ocupados = list(map(int, input().split()))
    else:
        assentos_ocupados = []
    return assentos_ocupados


subtracao = set(range_capacidade()) - set(assentos())
for i in subtracao:
    print(i, end=' ')