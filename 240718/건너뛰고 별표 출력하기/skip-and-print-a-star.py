n = int(input())

for i in range(1,n+1):
    print('*'*i, end='')
    print('\n')
for j in range(n-1,0,-1):
    print('*'*j, end='')
    print('\n')