a, b = map(int, input().split())

if a == 0 and b == 0 or a==0 and b==1:
    print('C')
elif a==1 and b==0:
    print('B')
else:
    print('A')