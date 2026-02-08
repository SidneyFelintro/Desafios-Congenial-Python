N = int(input())
M = tuple(map(int, input().split()))

for c in reversed(M):
    print(c, end=' ')