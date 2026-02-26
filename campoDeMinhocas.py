linhaseColunas = []
SomaDosValores = []

tamMatriz = list(map(int, input().split()))

for i in range(tamMatriz[0]):
    linhaseColunas.append(list(map(int, input().split())))

def MaiorEntreLinhaEColuna():
    for c in linhaseColunas:
        SomaDosValores.append(sum(c))

    for valores in zip(*linhaseColunas):
        SomaDosValores.append(sum(valores))
    return max(SomaDosValores)

print(MaiorEntreLinhaEColuna())