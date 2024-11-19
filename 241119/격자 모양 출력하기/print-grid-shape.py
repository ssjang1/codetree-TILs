n, m = map(int, input().strip().split(' '))

arr2d = [[0 for _ in range(n)] for _ in range(n)]
points = []
for _ in range(m):
    row,col=map(int,input().split(' '))
    points.append([row-1,col-1])

for i,j in points:
    arr2d[i][j] = (i+1)*(j+1)

for i in range(n):
    for j in range(n):
        print(arr2d[i][j], end=' ')
    print()