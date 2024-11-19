n = int(input())

arr2d=[[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    for j in range(0,i+1):
        arr2d[i][j]=1

for i in range(n):
    for j in range(0,i+1):
        if i>=1 and j>=1:
            arr2d[i][j] = arr2d[i-1][j-1] + arr2d[i-1][j]

for i in range(n):
    for j in range(n):
        if arr2d[i][j] != 0:
            print(arr2d[i][j], end=' ')
    print()