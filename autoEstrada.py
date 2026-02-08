soma= 0

N = int(input())
G = str(input()).upper().strip()

for i in G:
    if i == 'D':
        soma+= 0
    elif i == 'A':
        soma+= 1
    elif i == 'C':
        soma+= 2
    elif i == 'P':
        soma+= 2
    else:
        print('Valor invalido')
print(soma)