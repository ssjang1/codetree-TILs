n = int(input())

for i in range(1,n+1):
    print(' '*2*(n-i),end='')
    print(' '.join('@'*i))
for j in range(n-1,0,-1):
    print(' '.join('@'*j))