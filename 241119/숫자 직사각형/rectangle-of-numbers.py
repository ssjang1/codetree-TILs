n,m = map(int,input().strip().split(' '))

arr2d = [[0 for i in range(m)] for j in range(n)]

start = 1
for i in range(n):
    for j in range(m):
        arr2d[i][j] = start
        start +=1

for row in arr2d:
    for elem in row:
        print(elem, end=' ')
    print()