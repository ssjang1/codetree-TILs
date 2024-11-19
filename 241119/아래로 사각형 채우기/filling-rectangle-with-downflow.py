n = int(input())

arr2d=[[0 for _ in range(n)]for _ in range(n)]

num = 1
for i in range(n):
    for j in range(n):
        arr2d[j][i] = num
        num +=1

for i in range(n):
    for j in range(n):
        print(arr2d[i][j],end=' ')
    print()