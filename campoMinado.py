lista =[]

n = int(input())
for i in range(n):
    z = int(input())
    lista.append(z)

newList = [0] * len(lista)

for i, v in enumerate(lista):
    if v >= 1:
        if i:
            if i > 0:
                newList[i-1] += 1
            newList[i] += 1
            if i < len(lista)-1:
                newList[i+1] += 1
for v in newList:
    print(v)