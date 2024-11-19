n,m = map(int,input().strip().split(' '))

arr2d = [[0 for _ in range(m)]for _ in range(n)]

num = 0
for j in range(m):
    for i in range(n):
        if j%2 ==0:
            arr2d[i][j]=num
            num +=1
        else:
            arr2d[n-1-i][j]=num
            num+=1

for row in arr2d:
    for elem in row:
        print(elem, end =' ')
    print()