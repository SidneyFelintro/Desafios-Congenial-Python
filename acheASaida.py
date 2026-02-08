n = str(input(''))


if n == 'esquerda direita' or n == 'direita direita':
    print('Tente novamente')
elif n == 'direita esquerda':
    print('Achou')
elif n == 'esquerda esquerda':
    print('Morreu')
else:
    print('direções inválidas.')