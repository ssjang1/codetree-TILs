n = int(input())

for i in range(1,n+1):
    if i == 1:
        print(' '.join('*'*n))
    else:
        print(' '.join('*'*(i-1)),end='')
        print(' '*(2*n-1-(2*i-2)),end='')
        print('*')