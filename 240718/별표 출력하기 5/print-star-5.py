n = int(input())

for i in range(n,0,-1):
    for j in range(i):
        if j+1 != i:
            print('*'*i, end=' ')
        else:
            print('*'*i)