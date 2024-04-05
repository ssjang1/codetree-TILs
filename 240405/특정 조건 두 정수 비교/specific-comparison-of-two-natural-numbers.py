a,b = map(int,input().split(' '))

if a<b:
    first = 1
else:
    first = 0


if a==b:
    second =1
else:
    second =0

print(' '.join([str(first),str(second)]))