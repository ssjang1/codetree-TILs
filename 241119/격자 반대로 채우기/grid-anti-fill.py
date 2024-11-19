n = int(input())

num = 1

arr2d = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i%2 ==1:
            arr2d[j][n-1-i] = num
            num+=1
        else:
            arr2d[-j-1][n-1-i] = num
            num +=1


for row in arr2d:
    for elem in row:
        print(elem,end=' ')
    print()