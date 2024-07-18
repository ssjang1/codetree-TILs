n = int(input())

for i in range(n,0,-1):
    print(' '*(n-i)*2,end='')
    print(' '.join('*'*(2*i-1)))