a,b,c = map(int, input().split(' '))

is_true = False
for i in range(a,b+1):
    if i % c ==0:
        is_true = True

if is_true:
    print('NO')
else:
    print('YES')