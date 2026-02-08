tp1 = tuple(map(int, input().split()))
tp2 = tuple(map(int, input().split()))

resultado = tuple(x + y for x,y in zip(tp1, tp2))
print(*resultado)