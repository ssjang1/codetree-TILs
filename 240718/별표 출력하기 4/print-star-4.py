n = int(input())

for i in range(n,0,-1):
    print(' '.join('*'*i))
for j in range(2,n+1):
    print(' '.join('*'*j))