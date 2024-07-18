n = int(input())

for i in range(1,n+1):
    print(' '*(n-i)*2,end='')
    print(' '.join('*'*(2*i-1)))