z = tuple(map(str, input().split()))
g = tuple(map(str, input().split()))

if g == ('e', 'd'):
    print('Bloqueado')
else:
    if z == ('e', 'd'):
        print('Driblado')
        if g == ('d', 'd'):
            print('...e o goleiro pega')
        elif g == ('d', 'e'):
            print('Gol')