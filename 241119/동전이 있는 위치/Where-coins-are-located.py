n,m= map(int, input().strip().split(' '))

points =[]

for i in range(m):
    a,b = list(map(int,input().strip().split(' ')))
    points.append([a,b])

arr2d = [[0 for _ in range(n)]for _ in range(n)]
for p in points:
    i =p[0]-1
    j =p[1]-1
    arr2d[i][j]=1

for i in range(n):
    for j in range(n):
        print(arr2d[i][j],end=' ')
    print()
