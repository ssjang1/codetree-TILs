n = int(input())

for i in range(1,n+1):
    if i %2==0 or i%2==3:
        print(1, end=' ')
    else:
        print(0, end=' ')