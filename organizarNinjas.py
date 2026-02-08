def frente_ninja():
    frentes = int(input())
    ninjas = tuple(map(int, input().split()))

    for i, c in enumerate(reversed(ninjas)):
        indice = len(ninjas) - 1 - i
        print(f'{indice + 1}: {c}')

    return

frente_ninja()