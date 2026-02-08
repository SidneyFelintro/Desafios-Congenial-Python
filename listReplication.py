lista =[]

for c in range(5):
    N = int(input())
    if N not in lista:
        lista.append(N)

for c in sorted(lista):
    for i in range(3):
        print(c)