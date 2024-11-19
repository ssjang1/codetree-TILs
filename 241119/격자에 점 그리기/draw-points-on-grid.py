n,m = map(int,input().strip().split(' '))

arr2d = [[0 for _ in range(n)] for _ in range(n)]

points = []
for i in range(m):
    a,b= map(int,input().strip().split(' '))
    points.append([i+1,a-1,b-1])

for value, row, col in points:
    arr2d[row][col]=value

for i in range(n):
    for j in range(n):
        print(arr2d[i][j],end=' ')
    print()