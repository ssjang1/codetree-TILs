h, w = map(int, input().split(' '))
b = int(10000*w/(h**2))
if b >=25:
    print(b)
    print('Obesity')
else:
    print(b)