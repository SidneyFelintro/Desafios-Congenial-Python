soma = 0
N = tuple(map(int, input().split()))
for c in N:
  soma += c

soma =  2* N[0] - soma
print(soma)