cont = 0

N = int(input())
G = str(input()).upper().strip()
R = str(input()).upper().strip()

for g, r in zip(G, R):
    if g == r:
        cont += 1
print(cont)