a,b = map(int, input().split(' '))

is_true = False

for i in range(a,b):
    if 1920 % i ==0 and 2880 % i ==0:
        is_true = True
        print(1)
        break

if not is_true:
    print(0)