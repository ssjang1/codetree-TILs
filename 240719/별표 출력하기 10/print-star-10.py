n = int(input())

for i in range(0,n-1):
    if i%2 == 1:
        print(' '.join('*'*int(n-(i-1)/2)))
    else:
        print(' '.join('*'*int(1+(i/2))))

for j in range(n,-1,-1):
    if j%2 == 1:
        print(' '.join('*'*int(n-(j-1)/2)))
    else:
        print(' '.join('*'*int(1+(j/2))))