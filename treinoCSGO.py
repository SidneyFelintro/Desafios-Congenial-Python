lista = ()
resultado = soma = cont =  0

N = int(input())

try:
    P = list(map(int, input().split()))
except EOFError:
     P = []
lista = P


soma += sum(lista)

try:
    C = int(input())
except EOFError:
    C = 2

for n in lista:
    if n == C:
        cont += 1

resultado = soma - 2 *(C * cont)
print(resultado)