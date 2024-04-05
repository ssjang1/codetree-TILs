a,b,c = map(int, input().split(' '))

first = int(a == min([a,b,c]))

second = int(a==b==c)

print(' '.join([str(first),str(second)]))