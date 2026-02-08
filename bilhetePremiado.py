lista = []
encontrou = False

pessoas = int(input())

fase = list(map(int, input().split()))
lista.append(fase)

valor = int(input())

for p, i in enumerate(lista[0]):
    if valor == i:
        print('Número da poltrona do vencedor:', p)
        encontrou = True
        
if encontrou == False:
    print('Não há vencedor')